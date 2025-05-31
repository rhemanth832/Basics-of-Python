#Factorial of a no
import math
a=int(input('Enter the No: '))
print(math.factorial(a))
#(OR)
fact=1
a=int(input('Enter the No: '))
for i in range(1,a+1):
    fact=fact*i
print(fact)
