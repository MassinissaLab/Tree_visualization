class BinHeap1:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    def insert(self,k):
        if k not in self.heapList:
            self.heapList.append(k)
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def maxChild(self,i):
            try:
                if self.heapList[i*2] > self.heapList[i*2+1]:
                    return i * 2
                else:
                    return i * 2 + 1
            except:
                return i * 2
    def delMax(self):
        if len(self.heapList)>1:
            retval = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.percDown(1)
            return retval
    def delete (self,k):
        pos=0
        for i in range(1,len(self.heapList)):
            if(self.heapList[i]==k):
                 pos=i 
        if (pos!=0):
            retval = self.heapList[pos]
            self.heapList[pos] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.percDown(pos)
            return retval
        return None
        

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
    def getedges(self,k):
        for i in range(1,len(self.heapList)):
            if(2*i<len(self.heapList)):
                tuple =(self.heapList[i],self.heapList[2*i])
                k.append(tuple)
            if(2*i+1<len(self.heapList)):
                tuple =(self.heapList[i],self.heapList[2*i+1])
                k.append(tuple)
    def recherche(self,val,w,r):
        for i in range(1,len(self.heapList)):
            if self.heapList[i]==val:
                r.append(val)
                return
            else:
                w.append(self.heapList[i])          
            
            
