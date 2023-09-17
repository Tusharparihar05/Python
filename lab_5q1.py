N=int(input("Enter any number: "))
if 1<=N<=20:
 i=1
 while i<=N:
    print(f"Multiplication table of{i}")
    j=1
    while j<=20:
        res=i*j
        print(f"{i}X{j}={res}")
        j+=1
    i+=1
else:
   print("Enter a number between 1 and 20:")
  