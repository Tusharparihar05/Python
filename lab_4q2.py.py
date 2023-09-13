x=int(input("Enter any number 1: "))
y=int(input("Enter any number 2: "))
N=int(input("Enter any number: "))
if x>y:
    print("invalid input")
else:
    i=x+1
    while i<y:
        if i%N==0:
            print("Numbers are",'=',i)
        i+=1
        
        
    
