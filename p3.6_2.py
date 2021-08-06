#if reverse of the word is same as the word , print palindrome
kalame=input()
tool=len(kalame)
malake=''
for i in range(1,tool+1):
    malake=malake+kalame[-i]
    print(malake)

if kalame==malake:
    print('palindrome')
else:
    print('not palindrome')

