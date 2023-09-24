N=str(input("Enter any sentence: "))
vowel="AEIOUaeiou"
count=0
nv_count=0
space=0
for i in N:
    for i in vowel:
        count+=1
        if i !=vowel:
            nv_count+=1 
        elif i=='  ' and i=="/n" and i=="/t":
            space+=1

print("The total vowels are: ",count)
print("The total nonvowels are: ",nv_count)




