N=int(input("Enter any number: "))
i=1
sum=0
while i<=N:
    sum=sum+(1/i)
    i=i+1
print(f'The sum of series{N}:{sum:.9f}')

