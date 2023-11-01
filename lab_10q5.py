def mylist(l1, b):
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = []
    n = []
    
    if b == 'r':
        a.extend(my_list[:l1])
        a.extend(my_list[l1:])
        return a

    if b == 'l':
        n.extend(my_list[l1:])
        n.extend(my_list[:l1])
        return n

print(mylist(4, 'r'))
print(mylist(4, 'l'))