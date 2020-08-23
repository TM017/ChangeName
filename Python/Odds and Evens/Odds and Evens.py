import random
while True:
  option = input("\nChoose odds(1) or evens(2): ")
  a = input("Choose a number between 1-1000: ")
  b = random.randint(1,1000)
  a = int(a)
  option = int(option)
  print("Computer chose ", b)
  remainder = (a+b)%2
  if remainder == 0: # even 
    if option == 1:
      print("Computer wins!")
    else:
      print("You win!")
  else: # odd
    if option == 2:
      print("Computer wins!")
    else:
      print("You win!")  
      