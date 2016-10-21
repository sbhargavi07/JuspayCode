from collections import Counter

values = []

values = list(map(int, input().split(',')))
values.sort()
values.reverse()
number = ''.join(map(str, values))
number = int(number)
print("{:,d}".format(number))
