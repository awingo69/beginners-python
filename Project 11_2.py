#!/usr/bin/env python3

from datetime import date, time, datetime
from datetime import timedelta


def display_title():
    print("Arrival Time Estimator")
    print()

def inputs():
    est_date = input("Estimated date of departure (YYYY-MM-DD): ")
    est_time = input("Estimated time of departure (HH:MM AM/PM): ")
    miles = int(input("Enter miles: "))
    mph = int(input("Enter miles per hour: "))
    print()
    return est_date,est_time,miles,mph

def travel_time(est_date, est_time, miles, mph):
    print("Estimated travel time")
    dep_str = est_date + " " + est_time
    dep_datetime = datetime.strptime(dep_str, "%Y-%m-%d %I:%M %p")
    
    hrs = int(miles/mph)
    minut = int(miles % mph )
    hrs2min= (hrs * 60)
    new_est_time= (hrs2min) + (minut)
    arrv_time = dep_datetime + timedelta(minutes= new_est_time)
    
    
    print(f"Hours: {hrs}")
    print(f"Minutes: {minut}")
    print(f"Estimated date of arrival: {arrv_time: %Y-%m-%d}")
    print(f"Estimated time of arrival: {arrv_time: %I:%M %p}")
    print()
    return dep_str, dep_datetime,hrs,minut,arrv_time

def main():
    display_title()
    choice = "y"
    while choice == "y":    
        est_date, est_time, miles, mph = inputs()
        travel_time(est_date, est_time, miles, mph)
        
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")        

if __name__ == "__main__":
            main()    