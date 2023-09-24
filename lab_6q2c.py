N=int(input("Enter any number: "))
x=int(input("Enter any number"))
sum=0
i=1
while i<=N:
    sum=sum+(x**i)/i
    i+=1
print(f'The sum of series{N}:{sum:.9f}')