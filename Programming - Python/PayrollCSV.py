import csv
word=''
f=open('D:\Programming - Python\SampleCSV.csv','r')
string=csv.reader(f)
print('File read from path : D:\Programming - Python\SampleCSV.csv\n')
print('Calculating the wages .......\n')
print('%-20s'%'Name','%-20s'%'Hours Worked','%-20s'%'Wage')
for row in string:
    wage=int(row[1])*int(row[2])
    print('%-20s'%row[0],'%-20s'%row[1],'%-20s'%wage)
    
