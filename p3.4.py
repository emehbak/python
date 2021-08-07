hello='hello'
vorodi=input()
vorodi=vorodi.lower()
new=''
for i in vorodi:
    if i in hello:
        new=new+i
h=new.find('h')
e=new.find('e',h+1)
ll=new.find('l',e+1)
ll_2=new.find('l',ll+1)
o=new.find('o',ll_2+1)
if ((h<e) and (e<ll) and (ll<ll_2) and (ll<o)):
    print('YES')
else:
    print('NO')
