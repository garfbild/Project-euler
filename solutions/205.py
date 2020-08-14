import matplotlib.pyplot as plt
import numpy as np
from operator import add

def Statistics(a,b):
    # a sides on dice
    # b is number of dice
    DiceDigts = [0]*(a*b + 1)
    DiceDigitsFrequency = []
    DiceDigitsProbability = []
    DiceDigitsLabels = []

    for n in range(a**b):
        s = 0
        for d in range(b):
            c = a**d
            s += int((n - n%c)/c %a) + 1
        DiceDigts[s] += 1
        DiceDigitsFrequency.append(s)
    SumDiceDigit = sum(DiceDigts)
    for j in range(len(DiceDigts)):
        if DiceDigts[j] != 0:
            DiceDigitsProbability.append(DiceDigts[j]/SumDiceDigit)
        else:
            DiceDigitsProbability.append(0)
        DiceDigitsLabels.append(j)
    return DiceDigitsLabels,DiceDigitsProbability

FourLabels,FourProbability = Statistics(4,9)
SixLabels,SixProbability = Statistics(6,6)

# fig, ax = plt.subplots()
# barwidth = 0.35
# tempLabels = list(map(add,SixLabels ,([barwidth]*len(SixLabels))))

# plt.bar(FourLabels,FourProbability, width = barwidth)
# plt.bar(tempLabels,SixProbability, width = barwidth)
#
# plt.show()

total = 0
for c in range(len(SixProbability)):
    total += SixProbability[c]*sum(FourProbability[c+1:])

print(total)
