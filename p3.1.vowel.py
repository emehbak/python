vowel='aeiou'
vorodi=input()
vorodi=vorodi.lower()
consonant=''
for i in vorodi:
    if i not in vowel:
        consonant=consonant+'.'+i


print(consonant)
