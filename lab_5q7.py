num=int(input("Enter any number: "))
row=0
while row<num:
    space=num-row-1
    while space>0:
        print(end=' ')
        space=space-1
    st=row+1
    while st>0:
        print('*',end=' ')
        st=st-1
    row=row+1
    print()


