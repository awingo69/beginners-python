#!/usr/bin/env python3
import random


print("Blackjack")
print()

card_num = { 1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9:
        '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King' }
card_suite = { 'c': 'Clubs','h': 'Hearts', 's': 'Spades', 'd': 'Diamonds' }

class Card:
        def __init__(self, rank, suit):
                self.rank = rank
                self.suit = suit
        def __str__(self):
                return(card_num[self.rank]+" Of "+card_suite[self.suit])
        def getRank(self):
                return(self.rank)
        def getSuit(self):
                return(self.suit)
        def blackjack_score(self):
                if self.rank > 9:
                        return(10)
                else:
                        return(self.rank)
def show_of_hands(hand):
        for card in hand:
                print(card)
def show_count(hand):
        print("Count: "+str(count_hand(hand)))
def count_hand(hand):
        count_hand=0
        for card in hand:
                count_hand += card.blackjack_score()
        return(count_hand)
       
card_deck    = []
suits = [ 'c','h','d','s' ]
hand    = { 'dealer': [],'human': [] }
for suit in suits:
        for rank in range(1,14):
                card_deck.append(Card(rank,suit))
def hit_stand():
        user_input = ''
        if user_input == 'hit':
                hand['human'].append(card_deck.pop(0))
                if count_hand(hand['human']) > 21:
                        human_turn = False
                        human_turn_end = True
        elif user_input == 'stand':
                human_turn = False                    
play = True
random.shuffle(card_deck)
random.shuffle(card_deck)
random.shuffle(card_deck)
hand['human'].append(card_deck.pop(0))
hand['dealer'].append(card_deck.pop(0))
hand['human'].append(card_deck.pop(0))
hand['dealer'].append(card_deck.pop(0))
human_turn = True
human_turn_end = False

print('DEALER\'S SHOW CARD:'+'\n'+str(hand['dealer'][-1]))
print()
print('YOUR CARDS:')
show_of_hands(hand['human'])
show_count(hand['human'])
print()

if play is True:
        hit_stand()
user_input = ''
if user_input == 'hit':
        hand['human'].append(card_deck.pop(0))
        if count_hand(hand['human']) > 21:
                human_turn = False
                human_turn_end = True
elif user_input == 'stand':
        human_turn = False            

dealer_turn = True
dealer_turn_end = False
while not human_turn_end and dealer_turn:
        if count_hand(hand['dealer'])<17:
                hand['dealer'].append(card_deck.pop(0))
        else:
                dealer_turn = False
                if count_hand(hand['dealer'])>21:
                        dealer_turn = False
                        dealer_turn_end = True

print()
print("DEALER'S TURN:")
show_of_hands(hand['dealer'])
show_count(hand['dealer'])
print()

print("YOUR CARDS:")
show_of_hands(hand['human'])
show_count(hand['human'])
print()
if human_turn_end:
        print('You Busted. Dealer Wins!')
elif dealer_turn_end:
        print('Yay! The Dealer Busted. You Win!')
elif count_hand(hand['human']) > count_hand(hand['dealer']):
        print('Yay! You Win!')
else:
        print('Dealer Wins!')
print()


    
                        
    

def main():
        choice = "y"
        while choice == "y":
                    
        
                       
                choice = input("Play again? (y/n): ")
        print()
        
        del hand['dealer'][:]
        del hand['human'][:]
        
        print("Come back soon!")        
        

if __name__ == "__main__":
    main()    
    