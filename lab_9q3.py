l=[]
r=int(input("Enter any number: "))
c=int(input("Enter any number: "))
for i in range(0,r):
    l.append([])
    for j in range(0,c):
        l[i].append(0)
        l[i][j]=int(input("Enter numbers : "))
print(l)
        
