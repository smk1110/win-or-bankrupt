import random

total_times = 0
success_times = 0
start = int(input("Enter your start point. : "))
target = int(input("Enter your target point. : "))
winning_possibility = int(input('''Enter winning possibility. 
(If you win, you get 1 point, 
if you lose, you lose 1 point. 
Set it to an integer between 0 and 100) : ''')) / 100
possibility = 0
while True:
  balance = start
  while True:
    if random.random() < winning_possibility:
          balance+= 1 #win
    else:
      balance -= 1 #lose
    
    if balance == 0: #bankrupt
      total_times += 1
      break
    if balance == target: #success
      success_times += 1
      total_times += 1
      break
  possibility = success_times/total_times
  print(possibility)

  
  

  
  