#get the input and count the input 
load=dict()
n=int(input())
for i in range(0,n):
    insert=input()
    load[insert]=load.get(insert,0)+1


for i in load.keys():
    print(i,load[i])
