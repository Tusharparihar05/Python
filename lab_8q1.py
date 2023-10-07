'''def find_sum_of_elements(input_list):
    sum_result = 0
    length = 0
   

    for i in input_list:
        length += 1

    for num in input_list:
        sum_result += num
        
        return sum_result
    

user_input = input("Enter a list of integers separated by spaces: ")
input_list = [int(x) for x in user_input.split()]


result = find_sum_of_elements(input_list)
print("Sum of elements in the list:", result)'''

n = int(input("enter (length of list of integers):"))
l=list()
sum = 0 
product = 1

for i in range(n):
    l.append(int(input("enter a integer: ")))

for a in (l):
    sum = sum + a
for b in (l):
    product=product*b


print(f"the list of the integers {l}")
print(f"the sum of the elements of the list is {sum}")

print(f"the product of the elements of the list is product {product}")
a=l[0]
m=a
for d in l:
    if d>a:
        m=d
print(m)

        

    
