
#if number of upper case in the input is more than lower case,
# it writes the whole input with upper case and vise versa
vorodi=input()
lower_case=0
upper_case=0
for i in vorodi:
    if i>i.upper():
        lower_case=lower_case+1
    elif i<i.lower():
        upper_case=upper_case+1

if lower_case>=upper_case:
    print(vorodi.lower())
else:
    print(vorodi.upper())


