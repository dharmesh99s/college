element = [10,20,56,0,60]
x = bytes(element)

print(x[0])
x[0]=22 #we can not modifie bytes data type

for i in x:
    print(i)