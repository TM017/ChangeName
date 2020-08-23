#Guess a Number between 1 and 100
print("This is a fun program where you have to guess a number between 1 - 10!")
import random
Correct_Anwser = random.randint(1,11) 
while True:
  print("Type your guess here, then press enter:")
  Guess = int(input())
  if Guess > 10:
    Guess = 10
  if Correct_Anwser > Guess:
    print("Nope, but good guess, your guess is less than the actual number")
  elif Correct_Anwser < Guess:
    print("Nope, but good guess, your guess is more than the actual number")
  else:
      print("Yay you got it!!!")
      break 
  
