#Kabedi team 
player=int(input())
num_play=input()
l=num_play.split()
for i in range(0,len(l)):
    l[i]=int(l[i])

for i in l:
    if i>2:
        l.remove(i)
team=len(l)//3
print(team)
