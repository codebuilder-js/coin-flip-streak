import random

STREAK = 6

numberOfStreaks = 0
tailStreak = 0
headStreak = 0

headsAndTailsList = []

for experimentNumber in range(1000):
  # Code that creates a list of 100 'heads' or 'tails' values
  coinFlip = random.randint(0, 1)

  if coinFlip == 0:
    headsAndTailsList.append('H')
  elif coinFlip == 1:
    headsAndTailsList.append('T')

# Code that checks if there is a streak of 6 heads or tails in a row
for i in range(len(headsAndTailsList)):
  if headsAndTailsList[i:i+STREAK] == ['H'] * STREAK:
    headStreak += 1
    numberOfStreaks += 1
  elif headsAndTailsList[i:i+STREAK] == ['T'] * STREAK:
    tailStreak += 1
    numberOfStreaks += 1

print('Head Streak: ' + str(headStreak))
print('Tail Streak: ' + str(tailStreak))
print('Total Streak: ' + str(numberOfStreaks))
print('Chance of streak: %s%%' % (numberOfStreaks / 100))