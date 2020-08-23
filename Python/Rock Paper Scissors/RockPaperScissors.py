import random
import replit
import time
replit.clear()
print("Starting game of Rock, Paper and Scissors!!!")
while True:
  a = input("Put rock, paper, or scissors:")
  options = ["rock", "scissors", "paper"]
  computer_choice = options[random.randint(0, 2)]
  print("computer chose", computer_choice)
  if a == "rock":
    if computer_choice == "rock":
      print("it is a tie")
    elif computer_choice == "paper":
      print("computer wins")
    else:
      print("you win")
  elif a == "paper":
    if computer_choice == "paper":
      print("it is a tie")
    elif computer_choice == "rock":
      print("you win")
    else:
      print("computer wins")
  else:
    if computer_choice == "paper":
      print("you win")
    elif computer_choice == "scissors":
          print("it is a tie")
    else:
      print("computer wins")
  time.sleep(3)
  replit.clear()

