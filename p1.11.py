def maghsom(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return(count)


old_tedad=0
old_addad=0
for i in range(1,20):
    addad=int(input())
    tedad=maghsom(addad)
    if tedad>old_tedad:
        old_tedad=tedad
        old_addad=addad

print(old_addad, old_tedad)