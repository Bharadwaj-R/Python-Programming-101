password=input('enter the password : ')
check1=0
check2=0
check3=0
check4=0
check5=0
for char in password:
    if char.isdigit():
        check1=1
    elif char.isalpha():
        if char<='Z':
            check2=1
        elif char<='z':
            check3=1
    elif char=='$' or char=='#' or char=='@':
        check4=1
if len(password)<=16 and len(password)>=6:
    check5=1
if check1==1 and check2==1 and check3==1 and check4==1 and check5==1:
    print('valid format')
else:
    print('invalid format')
    
