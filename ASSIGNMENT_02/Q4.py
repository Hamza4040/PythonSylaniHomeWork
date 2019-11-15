l=[1,2,3,4,5,6,56,65,'a']
sum=0
n=len(l)
for i in range(n):
    if type(l[i])==int:
        sum+=l[i]

print(sum)
