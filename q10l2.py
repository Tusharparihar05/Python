# number = int(input("enter a number between 1 and 86400: "))
number = 70000
second = number%60
hours = number//3600
minutes = int(abs(hours-(number/3600))*60)
print(hours,minutes,second)
# print(number/60*60)
# print(minutes)
