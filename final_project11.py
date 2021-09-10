import csv
from collections import OrderedDict 
from statistics import mean
def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        l=csv.reader(f)
        d1=dict()
        for i in l:
            name=i[0]
            number=i[1:]
            for i in range(0,len(number)):
                number[i]=float(number[i])
            av=mean(number)
            d1[name]=av
            od=OrderedDict(d1)
    for z in od:
        output=str(z)+','+str(od[z])   #Task1
        with open(output_file_name,'a') as fout:
            fout.write(output+'\n')

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        l=csv.reader(f)
        d1=dict()
        for i in l: 
            name=i[0]
            number=i[1:]
            for i in range(0,len(number)):
                number[i]=float(number[i])   
            av=mean(number)
            d1[name]=av
            od=OrderedDict(d1)
    a = sorted(od.items(), key=lambda x: x[1])
    for p,q in a:
        if 
        tsk2=str(p)+','+str(q)
        with open(output_file_name,'a') as fout:
            fout.write(tsk2+'\n')


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as f:
        l=csv.reader(f)
        d1=dict()
        for i in l: 
            name=i[0]
            number=i[1:]
            for i in range(0,len(number)):
                number[i]=float(number[i])   
            av=mean(number)
            d1[name]=av
            od=OrderedDict(d1)

    b = sorted(od.items(), key=lambda x: x[1],reverse=True)
    rev=b[:3]
    for e,f in rev:
        tsk3=str(e)+','+str(f)
        with open(output_file_name,'a') as fout:
            fout.write(tsk3+'\n')

def calculate_three_worst(input_file_name, output_file_name):
        with open(input_file_name) as f:
            l=csv.reader(f)
            d1=dict()
            for i in l: 
                name=i[0]
                number=i[1:]
                for i in range(0,len(number)):
                    number[i]=float(number[i])   
                av=mean(number)
                d1[name]=av
                od=OrderedDict(d1)
                a = sorted(od.items(), key=lambda x: x[1])
                a2=a[:3]

        for x,y in a2:
            tsk4=str(y)   
            with open(output_file_name,'a') as fout:
                    fout.write(tsk4+'\n')
def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        l=csv.reader(f)
        d1=dict()
        l3=[]
        for i in l: 
            name=i[0]
            number=i[1:]
            for i in range(0,len(number)):
                number[i]=float(number[i])   
            av=mean(number)
            d1[name]=av
            od=OrderedDict(d1)
    l3=list(od.values())
    task5=str(mean(l3))
    with open(output_file_name,'a') as fout:
        fout.write(task5+'\n')



calculate_averages('/tmp/file.csv','/tmp/task1.csv')
calculate_sorted_averages('/tmp/file.csv','/tmp/task2.csv')
calculate_three_best('/tmp/file.csv','/tmp/task3.csv')
calculate_three_worst('/tmp/file.csv','/tmp/task4.csv')
calculate_average_of_averages('/tmp/file.csv','/tmp/task5.csv')
