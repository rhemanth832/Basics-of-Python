
n=int(input('Enter the No: '))
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)

#count the digits

n=int(input('Enter the No: '))
sum=0
while n>0:
    d=n%10
    sum=sum+1 #instead of d replace as 1 (to count digits).
    n=n//10
print(sum)