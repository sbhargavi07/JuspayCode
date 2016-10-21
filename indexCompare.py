
values = []
n = input()
n = int(n)
tempVar=0
for tempVar in range(n):
    temp = input()
    values.append(temp)


for key in values:
    if values[int(key)] == key:
        print(key)
