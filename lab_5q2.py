N=int(input("Enter any number: "))
if N<=0:
    print("Enter a valid number: ")
else:
    i=1
    while i<=1000:
        if i%N==0:
            i+=1
            continue
        print(i,end=' ')
        i+=1
