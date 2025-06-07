thelist=list(input('enter the string :\n'))
choice=int(input('enter 1 to rotate right and -1 to rotate left : '))
rotate=int(input('enter the no of characters to rotate : '))
if choice==1:
    thelist=thelist[-rotate:]+thelist[:len(thelist)-rotate]
    print('the new list is :',thelist)
elif choice==-1:
    thelist=thelist[rotate:]+thelist[:rotate]
    print('the new list is :',thelist)
