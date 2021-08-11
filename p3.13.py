#enter n numbers it returns the formated 'sqrt' with 4 digit places
l=[]
n=int(input())
import math 
for i in range(0,n):
    number=int(input())
    root=math.sqrt(number)
    new_root='{:0.4f}'.format(root)
    l.append(new_root)

for i in l:
    print(i)
