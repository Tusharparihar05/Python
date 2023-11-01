'''Paragraph=str(input("Enter paragragh : "))
vowels="AEIOUaeiou"
count=0
for char in Paragraph:
    if char in vowels:
        count+=1
print('The frequency of Vowels' ,{count})

count_1=0
count_2=0
count_3=0
count_4=0
count_5=0

for i in Paragraph:
    if i=='A' or i=='a':
        count_1+=1
    elif i=='E' or i=='e':
        count_2+=1
    elif i=='I' or i=='i':
        count_3+=1
    elif i=='O' or i=='o':
        count_4+=1
    elif i=='U' or i=='u':
        count_5+=1

a={}
a.append(count_1)
a.append(count_2)
a.append(count_3)
a.append(count_4)
a.append(count_5)
print(a)
a.sort()
print(a)'''

Para=input("Enter any paragraph: ")
diction={}
vowels='AEIOUaeiou'
for char in Para:
    if char in vowels:
        diction[char]=Para.count(char)
print(diction)



    
