# 0 1 1 2 3 5 8 13
# a=0 b=1  : c=a+b
a=0
b=1
n=int(input('how many terms: '))
print (a,b,end=' ')
for i in range(n-2):
    c=a+b
    print(c,end=' ')
    a=b
    b=c