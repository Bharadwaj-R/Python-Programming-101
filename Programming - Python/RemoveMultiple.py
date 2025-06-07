thelist=list(input('enter a string input :\n'))
for char in thelist:
    count=thelist.count(char)
    for i in range(1,count):
        thelist.remove(char)
print('the new string is :\n',thelist[0:])

'''
a more optimised way of implementing can be using sets

thelist=list(input('enter a string input : '))
thelist=list(set(thelist))
'''
