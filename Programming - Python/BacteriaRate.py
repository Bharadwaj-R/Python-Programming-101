n=int(input('enter the initial amount of bacteria : '))
rate=int(input('enter the rate of growth (>0) : '))
tr=int(input('enter the time taken for that growth rate : '))
time=float(input('enter the number of hours of growth : '))
timeint=int(time//tr)
for i in range(timeint):
    n=n*rate
if (time-(timeint*tr))>0:
    n=n*(time-(timeint*tr))*(rate/tr)
print('the new number is : ',n)
