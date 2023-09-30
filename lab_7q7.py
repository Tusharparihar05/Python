s=str(input("Enter any sentence : "))
t=''
for i in s:
    if i not in t:
        t+=i
print(t)
 
    