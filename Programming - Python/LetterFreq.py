word=input('enter a word : ')
cmax=0
count=0
letter=''
for ch in word:
    for c in word:
        if c==ch:
            count+=1
        if cmax<count:
            cmax=count
            letter=ch
    count=0
print('the maximum occuring letter is',letter,'and it appears',cmax,'times')
