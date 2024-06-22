import random

possibility = 0
succeed_times = 0
total_times = 0
while True:
  a=random.randint(1,3)
  if a == 1:
    succeed_times += 1
  total_times += 1
  possibility = succeed_times/total_times
  print(possibility)