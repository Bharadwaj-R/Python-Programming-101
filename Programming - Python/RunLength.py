word=list(input('enter a word : '))
count=0
k=0
for i in range(len(word)):
    for j in range(i,len(word)):
        if word[i]==word[j]:
            count+=1
            if count>1:
                word[j]='*'
        else:
            break
    if word[i]!='*':
        word[k]=[count,word[i]]
        k=k+1
    count=0
if k<len(word):
    del word[k:]
print(word)
