from collections import Counter

values = []

n = input()
n = int(n)
counterVar = 0
tempVar = ""
for counterVar in range(n):
    tempVar = input()
    values.append(tempVar)
countValues = Counter(values)
#print(countValues)
for key,value in countValues.items():
    if value >1:
        print(key)
