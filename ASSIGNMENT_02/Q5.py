#==========First Method=============
L=[10,20,30,56,45,87,78]
L.sort()
print("Largest Number is: ",L[-1])

#==========Second Method============
L=[12,45,32,98,67]
max=L[0]
for a in L:
    if a>max:
        max=a
print("Largest Number is: ",max)
