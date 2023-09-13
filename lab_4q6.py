N=int(input("Enter any number: "))
a=0
while N>0:
    r=N%10
    N=N//10
    a=(10*a)+r
if a==N:
        print("It is Palindrome ")
else:
    print("It is not palindrome ")
