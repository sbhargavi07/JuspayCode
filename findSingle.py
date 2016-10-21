from collections import Counter
def findUnique(values):
    values_list = Counter(values)
    for keys,values in values_list.items():
        if values==1:
            print (keys)

values = []
n = input()
n = int(n)
tempVar=0
for tempVar in range(n):
    temp = input()
    values.append(temp)
findUnique(values)

