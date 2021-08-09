n=int(input())
old_list=''
for i in range(0,n):  #get input and put all input inside a file 
    input_list=input()
    old_list=old_list+' '+input_list

#convert to list
l=old_list.split()

#convert str to int inside the list
for i in range(0,len(l)):
    l[i]=int(l[i])

Happy=0
poor=0
n=n//2
for i in range(0,n):
    if (l[2*i]<l[2*i+2]) and l[2*i+1]>l[2*i+3]:
        Happy=Happy+1
       
    else:
        poor=poor+1
       

if Happy!=0:
    print('happy irsa')
elif poor!=0:
    print('poor irsa')

