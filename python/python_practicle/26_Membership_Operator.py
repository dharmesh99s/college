# Membeership IN Operator 
name = ["dharmesh","urmil","himanshu","smit"]
for names in name:
    print(names,end=" ")

print(" ")
postal = {'delhi:':110001,'chennai':600001,'amreli':365601}
for city in postal:
    print(city,postal[city])


# Membeership NOT IN Operator
x = 10
foo = [10,20,30,40,50]

if(x not in foo ):
    print("x is not present")
else:
    print("x is present")