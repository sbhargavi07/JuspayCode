from collections import Counter

values = []
n = input()
n = int(n)
tempVar=0
for tempVar in range(n):
    temp = input()
    values.append(temp)
values_list = Counter(values)
for keys,values in values_list.items():
    if values==1:
        print (keys)
