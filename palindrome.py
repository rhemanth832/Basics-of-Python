#check palindrome
a=input('Enter the element: ')
if a == a[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')
    #(OR)
a=input('Enter the String: ')
n=len(a)
flag=1
x=int(n/2)
for i in range(x):
    if (a[i]!=a[n-i-1]):
        flag=0
if (flag==1):
    print('yes')
else:
    print('no')