def isSubset(list1,list2):
    for val in list1:
        if val in list2:
            pass
        else:
            print("False")
            sys.exit()
    print("True")

list1 = []
n = int(input())
list2 = []
m = int(input())
tempVar = 0
for tempVar in range(n):
    temp = input()
    list1.append(temp)
for tempVar in range(m):
    temp = input()
    list2.append(temp)
isSubset(list1,list2)
