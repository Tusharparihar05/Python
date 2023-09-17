N=int(input("Enter any number: "))
num=0
i_count=0
n_count=0
while num!=-999:
    num=int(input("Enter numbers repeatedly: "))

    if num%N==0:
        n_count=n_count+1
    else:
        i_count=i_count+1
print("The numbers divisible are: ",n_count)
print("The numbers not divisble are: ",i_count)
         
