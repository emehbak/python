#30 math score calculation based on the result of game (3,1,0)
count1=0
count2=0
for i in range(1,31):
    score=int(input())
    if score==3:
        count1=count1+1
    elif score==1:
        count2=count2+1

final_score=3*count1+count2
winnings=count1
print(final_score,winnings)
