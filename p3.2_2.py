adad=input()
yek=adad.count('1')
doo=adad.count('2')
seh=adad.count('3')
yek_1=''
doo_1=''
seh_1=''
for i in range(1,yek+1):
    yek_1='1'+'+'+yek_1
for i in range(1,doo+1):
    doo_1='2'+'+'+doo_1
for i in range(1,seh+1):
    seh_1='3'+'+'+seh_1


x=yek_1+doo_1+seh_1
print(x[:-1])
