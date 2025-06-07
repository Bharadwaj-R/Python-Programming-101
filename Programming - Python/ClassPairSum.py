class PairSum:
    def __init__(self,inplist,target):
        self.inplist=inplist
        self.target=target
    def checkpair(self):
        for i in range(len(self.inplist)):
            for j in range(i+1,len(self.inplist)):
                if self.inplist[i]+self.inplist[j]==self.target:
                    print('pairs -',i,',',j)
inplist=[]
n=int(input('enter no. of elements : '))
for i in range(n):
    item=int(input('enter element : '))
    inplist.append(item)
target=int(input('enter target : '))
paircheck=PairSum(inplist,target)
paircheck.checkpair()
