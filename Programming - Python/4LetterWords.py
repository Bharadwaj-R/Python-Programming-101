f=open('D:\Programming - Python\Sample.txt','r')
string=f.read()
print('The original string is :\n\n',string,sep='')
string=string.split()
count=0
for i in range(len(string)):
    if len(string[i])==4:
        count+=1
print('no of 4 letterd words are :',count)
f.close()
