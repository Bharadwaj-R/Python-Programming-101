list1=['red', 'green', 'black', 'orange']
list2=['red', 'pink', 'green', 'white', 'black']
list3=['white', 'orange', 'pink', 'black']
print('the given lists are :\n',list1,'\n',list2,'\n',list3)
check1=[]
check2=[]
for colour in list1:
    for colourcheck in list2:
        if colourcheck==colour:
            check1.append(colour)
for colour in list2:
    for colourcheck in list1:
        if colourcheck==colour:
            check2.append(colour)
if check1==check2:
    print('true for list1 and list 2')
else:
    print('false for list 1 and list 2')

for colour in list2:
    for colourcheck in list3:
        if colourcheck==colour:
            check1.append(colour)
for colour in list3:
    for colourcheck in list2:
        if colourcheck==colour:
            check2.append(colour)
if check1==check2:
    print('true for list 2 and list 3')
else:
    print('false for list 2 and list 3')
