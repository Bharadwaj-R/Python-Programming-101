word=input('enter a string : ')
if len(word)<2:
    print('Empty String')
else:
    print(word[0],word[1],word[len(word)-2],word[len(word)-1])
