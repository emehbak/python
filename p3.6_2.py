#if reverse of the word is same as the word , print palindrome
vorodi=input()
tool=len(vorodi)
reverse=''
for i in range(1,tool+1):
    reverse=reverse+vorodi[-i]


if vorodi==reverse:
    print('palindrome')
else:
    print('not palindrome')
