number=int(input()) #enter a 3 digit number
reverse=int(str(number%10)+str((number%100)//10)+str(number//100))
reverse2=2*reverse
print(reverse2)
