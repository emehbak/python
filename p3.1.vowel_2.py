vowel='aeiou'
vorodi=input()
vorodi=vorodi.lower()
vorodi=vorodi.replace('a','')
vorodi=vorodi.replace('e','')
vorodi=vorodi.replace('i','')
vorodi=vorodi.replace('o','')
vorodi=vorodi.replace('u','')
consonant=''
for i in vorodi:
    consonant=consonant+'.'+i

print(consonant)
