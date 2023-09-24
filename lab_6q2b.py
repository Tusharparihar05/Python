N=int(input("Enter any number: "))
i=1
sum=0
fact=1
while i<=N:
    fact=fact*i
    i+=1
    sum=sum+(1/fact)
print(f'The sum of series{N}:{sum:.9f}')