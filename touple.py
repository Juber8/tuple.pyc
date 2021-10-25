#create empty touple
'''
x=()
print(x)

y=tuple()
print(y)

#write a tuple with diffrent deta types
s=('juber',False,2.5,12)
print(s)

#write a program tp create a tuple with number and print one items
tuplex=10,11,12,13,14
print(tuplex)
tuplex=11
print(tuplex)

tuplex=(45,58,58)
print(tuplex)
n1,n2,n3=(tuplex)
print(n1+n2+n3)

add new items in tuple

print(s)
s= s[1:3] + (10,20,50)
print(s)
s1=list(s)
s1.append(30)
print(s1)

#convert touple into string
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
s=''.join(tup)
print(s)

#write a program to get fourth element and get last element from list
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
toplex=tuplex[3]
print(toplex)
toplex=tuplex[-4]
print(toplex)

#write a program to crete colon of tuple
from copy import deepcopy
s = ("HELLO", 5, [], True)
print(s)
s1=deepcopy(s)
print(s1)

#Write a Python program to find the repeated items of a tuple
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count=tuplex.count(2)
print(count)

#Write a Python program to check whether an element exists within a tuple.
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(3 in tuplex)

#Convert list to tuple
listx = [5, 10, 7, 4, 15, 3]
tuple=tuple(listx)
print(tuple)

#Write a Python program to remove an item from a tuple.
s = ("w", 3, "r", "s", "o", "u", "r", "c", "e")
list1=list(s)
list1.remove("s")
print(list1)

s= (4, 6, 2, 8, 3, 1)
s1= s + (9,)
print(s1)
print(s)
'''
l=[10,20,30,40,50]
for i in l:
    if i==30:
        print(i)
        continue


