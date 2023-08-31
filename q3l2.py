x=int(input("Enter the number 1: "))
y=int(input("Enter the number 2: "))
if x<=0 or y<=0:
    print("invalid input")
if y%x==0:
    print("yes")
else:
    print("no")
