import random
import sys

streakLength = 6
streaks = 0
zeroStreaks = 0
oneStreaks = 0
iterations = int(sys.argv[1])
totalValues = (iterations * 100)
for experimentNumber in range(iterations):
        flips = []
        for i in range(100):
            flips.append(random.randint(0,1))
        # sliding window
        for i in range(100 - streakLength):
            # assume it is a streak, and check if it is not
            isStreak = True

            for j in range(i + 1, i + streakLength):
                if (flips[i] != flips[j]):
                    isStreak = False
                
            if isStreak:
                streaks += 1
                if flips[i] == 0:
                    zeroStreaks += 1
                else:
                    oneStreaks += 1

print('streaks: ' + str(streaks))
print('total values: ' + str(totalValues))
print(streaks / totalValues)
print('streaks of 1: ' + str(zeroStreaks) + '. streaks of 0: ' + str(oneStreaks))
