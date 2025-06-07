def ebill(units,costperunit):
    print('-'*40)
    total=units*costperunit
    print('%-20s'%('Name'),':','%15s'%(name))
    print('%-20s'%('Consumer ID'),':','%15s'%(cid))
    print('%-20s'%('Previous Reading'),':','%15s'%(prevread))
    print('%-20s'%('New Reading'),':','%15s'%(newread))
    print('%-20s'%('Units Consumed'),':','%15s'%(units))
    print('%-20s'%('Cost Per Unit'),':','%15s'%(costperunit))
    print('-'*40)
    print('%-20s'%('Total to be paid'),':','%15s'%(total))
    print('-'*40)
name=input('enter name of consumer : ')
cid=int(input('enter consumer ID : '))
prevread=int(input('enter previous meter reading : '))
newread=int(input('enter the new reading : '))
units=newread-prevread
costperunit=int(input('enter cost per unit : '))
ebill(units,costperunit)
