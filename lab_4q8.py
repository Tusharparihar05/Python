n=int(input("enter any number: "))
i=1
if n==1:
    print("it is not a prime")
else:
    while (i<n):
        if (n%i)==0:
            print("It is not prime: ")
        break
    else:
        print("It is prime: ")
        i=i+1

        
