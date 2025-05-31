ele=input('Enter the string: ')
a=ele.count('a')
e=ele.count('e')
i=ele.count('i')
o=ele.count('o')
u=ele.count('u')
print(a+e+i+o+u)

#or
a=input('Enter the string: ')
l=['a','e','i','o','u']
c=0
for i in a:
    if i in l:
        c=c+1
print(c)
