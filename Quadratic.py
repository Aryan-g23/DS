from cmath import sqrt
import time

print('Enter Data in this form : ax^2 + bx + c = 0')

a = int(input('Enter value of a'))
b = int(input('Enter value of b'))
c = int(input('Enter value of c'))
before=time.time()
root1 = (-b + sqrt(b^2-4*a*c))/(2*a)

root2 = (-b - sqrt(b^2-4*a*c))/(2*a)

if(root1.imag != 0):
    print('Complex')


elif root1.imag == 0 and root1!=root2 :
    print('Real and Different')


elif(root1==root2):
    print('Real and Equal')
    
print(root1,  root2)
after=time.time()
print("time=",(after-before))
