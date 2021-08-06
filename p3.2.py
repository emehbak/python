vorodi=input()

one=''
two=''
three=''
for i in vorodi:
    if i=='1':
        one=one+i+'+'
    elif i=='2':
        two=two+i+'+'
    elif i=='3':
        three=three+i+'+'


final=one+two+three
final=final[:-1]
print(final)
