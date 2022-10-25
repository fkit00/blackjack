import random 
import clear
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

def calculate_score(cards):
  sum_cards=sum(cards)
  if sum_cards==21:
    return 0
    
  if 11 in cards and sum_cards>21:
    cards.remove(11)
    cards.append(1)
    sum_cards=sum(cards)
 
  return sum_cards
  

for _ in range(2):
  new_cards= deal_card()
  user_cards.append(new_cards)
  
for _ in range(2):
  new_cards= deal_card()
  computer_cards.append(new_cards)


user_cards_score = calculate_score(user_cards)
computer_cards_score=calculate_score(computer_cards)

while not game_over:
    
  print(f"Your cards are {user_cards}, your score is {calculate_score(user_cards)}")
  print(f"The computers first card is  {computer_cards[0]}")
  
  if computer_cards_score == 0 or user_cards_score == 0 or user_cards_score>21 :
    game_over=True
  else:
    new_card=input(f"Your score is {user_cards_score}, would you like to pick another card? y/n  ")
    if new_card=='y':
      additional_card=deal_card()
      user_cards.append(additional_card)
      user_cards_score = calculate_score(user_cards)
      print(f"you picked {additional_card}")
    if new_card=='n':
      game_over=True

while computer_cards_score !=0 and computer_cards_score<17:
  additional_card=deal_card()
  computer_cards.append(additional_card)
  computer_cards_score=calculate_score(computer_cards)
  print(computer_cards_score)




def compare(computer_cards_score, user_cards_score):
  if computer_cards_score==user_cards_score:
    return "It's a draw!"
  elif computer_cards_score == 0:
    return "Lose, the house has Blackjack!"
  elif user_cards_score == 0:
    return 'Blackjack, you win!'
  elif user_cards_score>21:
    return 'You went over, you lose!'
  elif computer_cards_score>21:
    return 'House went over, you win!'
  elif user_cards_score>computer_cards_score:
    return 'You win!'
  else: 
    "you lose"

print(compare(computer_cards_score, user_cards_score))

again= input('Do you want to play again? y/n ')

if again == 'y':
  clear()
  game_over=False

  