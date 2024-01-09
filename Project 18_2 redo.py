#!/usr/bin/env python3

import tkinter as tk 
from tkinter import ttk, messagebox 

PrefData = []

def write_data():
    try:
        with open("PreferencesApp.txt", "r") as file:
            return True
    except FileNotFoundError:
        return False
        
def read_data():
        with open("PreferencesApp.txt","r", newline="") as file:
            info = file.read().splitlines() 
            PrefData.append(info[0])
            PrefData.append(info[1])
            PrefData.append(info[2])              
    
    
    
class PreferencesFrame(ttk.Frame):  
    def __init__(self, parent):
        ttk.Entry.__init__(self, parent) 
        self.parent = parent
        
        
    #string var for entry fields and errors
        self.name = tk.StringVar()
        self.language = tk.StringVar()
        self.autosave= tk.StringVar()
        self.nameError= tk.StringVar()
        self.languageError = tk.StringVar()
        self.autosaveError= tk.StringVar()     
        
    #labels
        self.label(root, 0, 0, 20, 5, "Name:")
        self.label(root, 1, 0,20,5, "Language:")
        self.label(root, 2, 0,20,5, "Auto Save Every X Minutes:")        
        
    # add var
        self.build(root, 0, 1,5,5, PrefData[0], self.name,"")
        self.build(root, 1, 1,5,5, PrefData[1], self.language,"")
        self.build(root, 2, 1,5,5, PrefData[2], self.autosave,"")  
        
    #add error var
        self.build(root, 0, 2,5,5, "", self.nameError,"label")
        self.build(root, 1, 2,5,5, "", self.languageError,"label")
        self.build(root, 2, 2,5,5, "", self.autosaveError,"label")        
        
        self.parent = parent           
    
        self.buildButtons()                        
        
    def buildButtons(self):
    #create the buttons 
        self.button(root, 4, 1, 0, "Save", self.error_check)
        self.button(root, 4, 1, 80,"Cancel", self.remove)         
        
    def build(self, master, row, column, X, Y, text, Field, lbl):    
        
        Field.set(text)
        if lbl == 'label':
            ttk.Label.__init__(self, master, textvariable=Field)
        else:
            ttk.Entry.__init__(self, master, textvariable=Field)
        self.master = master


        self.grid(row=row, column=column, sticky=tk.W, pady=(Y, 0), padx=(X, 10))        

    def button(self, master, row, column, X, text, command):               
        ttk.Button.__init__(self, master,text=text, command=command)
        self.master = master
        self.grid(row=row, column=column, sticky=tk.W, pady=(10, 0), padx=(X, 0))             
    
    def label(self, master, row, column, X, Y, text, alignment = tk.E): 
    
        ttk.Label.__init__(self, master, text=text)
        self.master = master
        self.grid(padx=(X, 0), pady=(Y, 0), row=row, column=column, sticky=tk.E)                                         
    
    def need_info(self,val):
        error = ""
        if val == "":
            error = "Required."
        else:
            error = ""
        return error
            
    def need_int(self,val):
        error = ""
        try:
            int(val)
        except ValueError:
            error = "Must be a valid integer"
        return error
    
#the block of error checks

    def error_check(self):
        self.message = "" # clear any previous error message 
    
        self.nameError.set(self.need_info(self.name.get()))
        if self.nameError.get() == "":
            self.name = (self.name.get()) 
        else:
            self.message = "error"
    
        self.languageError.set(self.need_info(self.language.get()))
        if self.languageError.get() == "":
            self.language = (self.language.get())
        else:
            self.message = "error"        
           
        self.autosaveError.set(self.need_int(self.autosave.get()))
        if self.autosaveError.get() == "":
            self.autosave = int(self.autosave.get())
        else:
            self.message = "error"         
            
    
        if self.message == "": # no errors
                       
            PrefData.clear()
            PrefData.append(self.name)
            PrefData.append(self.language)
            PrefData.append(self.autosave)
            
    
            self.save()
            self.remove()
    def save(self): 
        with open("PreferencesApp.txt", "w") as file:
            text =F"{PrefData[0]}\n{PrefData[1]}\n{PrefData[2]}"

            file.write(text)
            
        
    def remove(self):
        root.destroy()
        
if __name__ == "__main__":
    if write_data() == True:     
        read_data()
    else:
        #put blanks in Data list if no file
        PrefData.append("")
        PrefData.append("")
        PrefData.append("")    
    root =tk.Tk()
    root.title("Preferences")
    PreferencesFrame(root)
    root.mainloop()     