#to find out the maximum age and second maximum age
age1=0
age2=0
input_age=int(input())
while input_age!=-1:
    if input_age>age1:
        age2=age1
        age1=input_age
    elif input_age>age2:
        age2=input_age
    input_age=int(input())

print(age1,age2)
