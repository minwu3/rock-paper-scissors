rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

your_pick = int(input("What fo you choose? Tyype 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_pick = random.randint(0,2)

if your_pick == 0:
  print(rock)
  print(computer_pick)
  if computer_pick == 0:
    print(rock)
    print("A draw!")
  elif computer_pick == 1:
    print(paper)
    print("You lose.")
  else:
    print(scissors)
    print("You win!")  
  
elif your_pick == 1:
  print(paper)
  print(computer_pick)
  if computer_pick == 0:
    print(rock)
    print("You win!") 
  elif computer_pick == 1:
    print(paper)
    print("A draw!")
  else:
    print(scissors)
    print("You lose.")
    
else:
  print(scissors)
  print(computer_pick)
  if computer_pick == 0:
    print(rock)
    print("You lose.") 
  elif computer_pick == 1:
    print(paper)
    print("You win!")
  else:
    print(scissors)
    print("A draw!")
    
