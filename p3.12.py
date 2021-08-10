#dictionary , it get 5 input and interprets to correspondence 
load=dict()
n=int(input())  #enter the number words to translate
for i in range(0,n):
    x=input().split()
    load[x[0]]=x[1]

y=input().split()  #enter the sentence
z=''
for i in y:
    z=z+' '+load.get(i,i)
print(z)

