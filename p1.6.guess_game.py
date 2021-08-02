#chose a numebr, let sofware to find out the number in your mind
a=1
b=99
import random
guess=random.randint(a, b)
print('Is ',guess,' a correct answer? ')
print('Enter b for bigger, s for smaller and c for correct ')
answer=str(input('b,s or c?: '))
while answer!='c':
    if answer=='b':
        a=guess
        newguess=random.randint(a, b)
        print('Is ',newguess,' a correct answer? ')
    elif answer=='s':
        b=guess
        newguess=random.randint(a, b)
        print('Is ',newguess,' a correct answer? ')
    answer=str(input('b,s or c?: '))
    guess=newguess

print(guess,' is correct ')