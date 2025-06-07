def remove(tempdict):
    newdict={}
    keys=tempdict.keys()
    k=int(input('enter the max value : '))
    for key in keys:
        if tempdict[key].isdigit() and int(tempdict[key])<k:
            newdict[key]=tempdict[key]
        elif tempdict[key].isdigit() and int(tempdict[key])>=k:
            continue
        else:
            newdict[key]=tempdict[key]
    print(newdict)

n=int(input('enter the number of terms in dictionary : '))
thedict={}
for i in range(n):
    key=input('enter the key : ')
    val=input('enter the value : ')
    thedict[key]=val
remove(thedict)
