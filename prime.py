from sympy import *
no=int(input('Enter the Number: '))
b=isprime(no)
print(b)

#(OR)
no=int(input('Enter the Number: '))
x=int(no/2)
flag=0
for i in range(2,x+1):
    if no % i==0:
        flag=1
        print('Not Prime')
if flag==0:
    print('Prime')
#series of prime
no=int(input('Enter the Number: '))
for j in range(2,no+1):
    x = int(j / 2)
    flag = 0
    for i in range(2, x+1):
        if j % i == 0:
            flag=1;
            break;
    if flag == 0:
        print(j)
