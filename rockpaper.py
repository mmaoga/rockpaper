import random

print()

user_input = str(input("What is your name: ")).upper()

print ()

print(user_input, ", Welcome to the Rock, Paper, Scissors Game! Here is the winning guide for the game!! \n\n"
    +"Winning Rules of the game are as follows: \n"
    +"(1)Rock vs paper->paper wins \n"
    +"(2)Rock vs scissor->Rock wins \n"
    +"(3)Paper vs scissor->scissor wins \n\n")


player = 0
computer = 0
tie = 0
game = 1

choices = ["rock", "paper", "scissors"]

while True:
  random_index = random.randint(0,2)
  computer_choice = choices[random_index]

  player_choice = input("Rock, Paper, or Scissors? ").lower()
  while player_choice not in choices:
    player_choice = input("Invalid choice. Please try again: ").lower()
  
  print()
  print("Your choice:", player_choice)
  print("Computer's choice:", computer_choice)
  print()

  if player_choice == 'rock':
    if computer_choice == 'rock':
      print("It's a TIE! Both players Selected Scissors!!")
      tie+=1
    elif computer_choice == 'scissors':
      print("Rock beats Scissors! You WIN!!")
      player+=1
    elif computer_choice == 'paper':
      print("Paper beats Rock! You LOSE!!")
      computer+=1
  elif player_choice == 'paper':
    if computer_choice == 'paper':
      print("It's a TIE! Both players Selected Scissors!")
      tie+=1
    elif computer_choice == 'rock':
      print(" Paper beats Rock! You WIN!!")
      player+=1
    elif computer_choice == 'scissors':
      print("Scissors beat Paper! You LOSE!!")
      computer+=1
  elif player_choice == 'scissors':
    if computer_choice == 'scissors':
      print("It's a TIE Both players Selected Scissors!!")
      tie+=1
    elif computer_choice == 'paper':
      print("Scissors beat Paper! You WIN!!")
      player+=1
    elif computer_choice == 'rock':
      print("Rock beats Scissors!You LOSE!")
      computer+=1

  print()
  print("SCORES:")
  print("     Number of games WON by "+str(user_input) +":"+str(player)+"!")
  print("     .....")
  print("     Number of games WON by the computer: "+str(computer)+"!")
  print("     .....")
  print("     Number of games tied: "+str(tie)+"!")
  print("     .....")
  print("     The number of rounds played: "+str(game)+"!")
  print()

  repeat = input("Would you like to Play again? (Y/N) ").lower()
  while repeat not in ['y', 'n']:
    repeat = input("Invalid. Please try again: ").lower()
  
  if repeat == 'n':
    
    print()
    print ("Thank you for playing " +str(user_input) + ". We hope you enjoyed the game!\nGoodbye!")
    print ("\n..........\n")
    break

  else:
    game+=1

  print("\n............\n"+"ROUND --  " +str(game)+"!"+"\n............\n")
  print ()

 

