string=input('enter a string with all vowels only : ')
check=1
vowel=['a','e','i','o','u']
for letter in string:
    if letter not in vowel:
        check=0
        break
if check==0:
    print('string not accepted!!')
else:
    print('string accepted')
