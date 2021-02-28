#identity operator
a = 10
b = 20
print(id(a))
print(id(b))

#identity IS operator
a = 100
b = 100
if(a is b):
    print("id is same")
else:
    print("id is not same")


#identity IS NOT operator
a = [1,2,3,4]
b = [1,2,3,4]
if(a is not b):
    print("id is not same")
else:
    print("id is same")
