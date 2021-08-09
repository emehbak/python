#enter the integer it will give the shortest rout
load=input()
l=load.split()
for i in range(0,len(l)):
    l[i]=int(l[i])


l.sort()
l_max=max(l)
l_min=min(l)
n=l_max-l_min
print(n)
