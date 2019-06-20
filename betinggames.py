import random

money = 100

#Coin toss game
def coinFlip (bet, guess):
  print("Flipping coin...")
  outcome = random.randint(1,2)
  if outcome == 1:
    outcome = "heads"
    print(outcome)
  elif outcome == 2:
    outcome = "tails"
    print(outcome)
  if outcome == guess:
    print ("you win")
    return bet
  else:
    print ("you lose")
    return 0-bet

## cho han game
def ChoHan(bet, guess):
  print("Rolling dice...")
  dice1 = random.randint(1, 6)
  print(dice1)
  dice2 = random.randint(1, 6)
  print(dice2)
  if (dice1 + dice2) % 2 == 0:
    outcome = "Even"

  else:
    outcome = "Odd"
  print(outcome)
  if outcome == guess:
    print ("you win")
    return bet
  else:
    print ("you lose")
    return  0-bet

## this is for use in card drawing game to match card up to type
def cardmatch(number):
  if number == 1:
    return "Ace"
  elif number == 11:
    return "Jack"
  elif number == 12:
    return "Queen"
  elif number == 13:
    return "King"
  else:
    return str(number)


##card draw betting game
def cardduel(bet):
  print("Drawing your card:")
  playerCard = random.randint(1, 13)
  print(cardmatch(playerCard))
  print("Drawing my card:")
  computerCard = random.randint(1, 13)
  print(cardmatch(computerCard))
  if playerCard > computerCard:
    print ("you win")
    return bet
  elif playerCard == computerCard:
    print("Draw")
  else:
    print ("you lose")
    return  0-bet

##this will check bet not greater than money
def placeBet(bet, money):
  if bet > money:
    print("not enough funds!")
    return False
  else:
    return True


## function where you choose game
def playGame():
  print("Games Available:")
  print("1 Coin Toss")
  print("2 Cho Han")
  print("3 Card Dual")
  choice = int(input("Make your choice?"))
  amount = int(input("How much do you bet?"))
  if placeBet(amount, money) == True:
      print("Bet accepted")
  else:
      return 0
##what happens when select coin toss        
  if choice ==1:
    guess = int(input ("press 1 for heads or 2 for tails"))
    if guess ==1:
        return coinFlip(amount, "heads")
    elif guess == 2:
        return coinFlip(amount, "tails")
    else:
        print("Invalid choice")
        return 0
## cho han dice game chosen 
  elif choice ==2:
      guess = int(input ("press 1 for Odd or 2 for Even"))
      if guess ==1:
        return ChoHan(amount, "Odd")
      elif guess == 2:
        return ChoHan(amount, "Even")
      else:
        print("Invalid choice")
        return 0
##card gae chosen
  elif choice ==3:
      return cardduel(amount)
  else:
      print("End game")
      return 0
choice = 0

while choice <5:
    money+= playGame()
    
     
     
  
      


      

    
  







#Call your game of chance functions here
##money+= playGame()

#print("available funds")
print(money)

##coinFlip (10, "heads")
#print("available funds")
money += coinFlip(10, "heads")
#print(money)
#ChoHan(10, "Even")
#print("available funds")
print(money)

#cardduel(10)
