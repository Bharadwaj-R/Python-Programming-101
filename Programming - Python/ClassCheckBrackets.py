class Check:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def checkvalid(self):
        if self.start=='[' and self.end==']':
            return True
        elif self.start=='{' and self.end=='}':
            return True
        elif self.start=='(' and self.end==')':
            return True
        else:
            return False
inp=list(input('enter brackets : '))
if len(inp)%2==1:
    print('invalid')
else:
    ch=False
    for i in range(1,len(inp),2):
        obj=Check(inp[i-1],inp[i])
        ch=obj.checkvalid()
        if ch:
            pass
        else:
            break
    if ch:
        print('valid')
    else:
        print('invalid')
    
