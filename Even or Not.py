a=list(map(eval,input('Enter the elements: ').split(' ')))
flag=0
for i in a:
    if i %2==0:
        flag=1
        print('Contain Even')
if flag==0:
    print('Not Even')