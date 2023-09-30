Sen=str(input("Enter any sentence: " ))
words=str(input("Enter any word: "))
Sen=Sen.split()
l=len(Sen)
words_count=0
for i in range(0,l):
    if words in Sen[i]:
        words_count+=1
print(words_count)



        