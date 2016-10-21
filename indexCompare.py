
def comparekey(copy_list):
    for key in copy_list:
        try:
            if copy_list[int(key)] == key:
                print(key)
        except:
            pass        
values = []
n = input()
n = int(n)
tempVar=0
for tempVar in range(n):
    temp = input()
    values.append(temp)
comparekey(values)

