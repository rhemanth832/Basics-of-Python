n=int(input('Enter the No: '))
temp =n
sum=0
while n>0:
    d=n%10
    sum=sum+d*d*d
    n=n//10
if temp==sum:
    print(temp,' is Armstrong Number')
else:
    print(temp, ' is Not Armstrong')