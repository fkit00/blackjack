import random 
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


user_cards = []
computer_cards = []
game_over=False

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

for _ in range(2):
  new_cards= deal_card()
  user_cards.append(new_cards)
  
for _ in range(2):
  new_cards= deal_card()
  computer_cards.append(new_cards)

  
print(f"Your cards are {user_cards}")
print(f"The computer has {computer_cards[0]}")

def calculate_score(cards):
  sum_cards=sum(cards)
  if sum_cards==21:
    return 0
    
  if 11 in cards and sum_cards>21:
    cards.remove(11)
    cards.append(1)
    sum_cards=sum(cards)
 
  return sum_cards
  

user_cards_score = calculate_score(user_cards)
computer_cards_score=calculate_score(computer_cards)
print(f"Your score is {user_cards_score}")
print(f"The computer score is {computer_cards_score}")

if computer_cards_score == 0 or user_cards_score == 0 or user_cards_score>21 :
  game_over=True
else:
  new_card=input(f"Your score is {user_cards_score}, would you like to pick another card? y/n  ")
  if new_card=='y':
    additional_card=deal_card()
    user_cards.append(additional_card)
    user_cards_score = calculate_score(user_cards)
    print(f"you picked {additional_card}, your score is {user_cards_score}")

  


#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

