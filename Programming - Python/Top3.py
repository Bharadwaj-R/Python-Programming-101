n=int(input('enter the number of items : '))
maxval=0
inpdict={}
for i in range(n):
    inpdict['item'+str(i+1)]=float(input('enter the frequency : '))
print('top 3 frequency :')
for i in range(3):
    for key in inpdict:
        if inpdict[key]>maxval:
            maxval=inpdict[key]
            maxpos=key
    print(maxpos,maxval)
    del inpdict[maxpos]
    maxval=0
