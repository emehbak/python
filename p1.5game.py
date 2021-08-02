#in this game, software takes a random number and you guess a number between 1,99 to get the correct answer 
def game():
    import random
    javab=random.randint(1,99)
    name=input('Good:) , what is your name? ')
    print('OK ',name,' lets start...')
    hads=int(input('eneter a number between 1 and 99: '))
    while hads!=javab:
            if hads>javab:
                print('give smaller number ')
            elif hads<javab:
                print('give bigger number ')
            hads=int(input('eneter a number between 1 and 99: '))
    print(hads,' correct !... awesome :) ')

answer=str(input('do you want to play a "guess what" game? (y/n): '))
if answer=='y':
    game()
elif answer=='n':
    print('OK, Thnaks:)')

