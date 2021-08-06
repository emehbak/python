#if reverse of the word is same as the word , print palindrome
vorodi=input()
vorodi=vorodi.lower()
reverse=''
for i in vorodi:
  reverse=i+reverse


if vorodi==reverse:
  print('palindrome')
else:
  print('not palindrome')
