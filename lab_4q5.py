n=int(input("Enter any number: "))
i=1
fact=1
if n<0:
    print("Factorial of negative number is not defined! ")
else:
    while i<=n:
        fact=fact*i
        i=i+1
    print(fact)
