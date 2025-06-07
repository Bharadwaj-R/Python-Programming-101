char=input('enter one letter only:')
if (ord(char) in range(65,91)) or (ord(char) in range(97,123)):
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        print('lower case vowel')
    elif char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        print('upper case vowel')
    else:
        print('consonant')
else:
    print('invalid input')
