#dictionary , it get 5 input and interprets to correspondence 
load=dict()
n=int(input())
for i in range(0,n):
    x=input().split()
    load[x[0]]=x[1]

y=input().split()
z=''
for i in y:
    z=z+' '+load.get(i,i)
print(z)

