s=str(input("Enter any sentence: "))
print(s)
t=s.split()
l=len(t)
for i in range(-1,-l-1,-1):
    print(t[i],end=' ')
