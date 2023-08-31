a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
if a>b and a>c:
    print("The greatest number is: ",a)
if a<b and b>c:
    print("The greatest number is: ",b)
if (a<b and c>b) or (a>b and c>a):
    print("The greatest number is: ",c)
