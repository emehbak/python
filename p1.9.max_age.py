#gets the input ages and prints the maximum one , once entering -1
new_age=0
age=int(input())
while age!=-1:
    max_age=max(new_age,age)
    new_age=max_age
    age=int(input())

print(max_age)
