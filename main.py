import random

total_times = 0
success_times = 0
possibility = 0
value = [0,0,0,0,0]
a =input("Do you want to set to default? (Y/N) : ")
if a == 'Y':
  file = open("default.txt", "r")
  default_values = [line.rstrip() for line in file]
  print(default_values)
  for i in range(0, 5):
    value[i] = float(default_values[i])
elif a=='N':
  value[0] = float(input("Enter your start point. : "))
  value[1] = float(input("Enter your target point. : "))
  value[2] = float(input("How many points do you want to get if you win? : "))   
  value[3] = float(input("How many points do you want to lose if you lose? : "))   
  value[4] = float(input('Set the odds that you will win (between 0 and 1) : '))
else:
  print("enter Y or N")
  exit()
while True:
  balance = value[0]
  while True:
    if random.random() < value[4]:
          balance+= value[2] #win
    else:
      balance -= value[3] #lose
    
    if balance <= 0: #bankrupt
      total_times += 1
      break
    elif balance >= value[1]: #success
      success_times += 1
      total_times += 1
      break
  possibility = success_times/total_times
  print(possibility)