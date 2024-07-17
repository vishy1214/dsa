class Array(object):

    def __init__(self, initialsize):
        self._nArray = [None] * initialsize
        self._nASize = 0

    def insert(self,item):
        self._nArray[self._nASize] = item
        self._nASize += 1

    def get(self,index):
        return self._nArray[index]

    def delete(self,item):
        #find it, remove it and reduce the array size else return false
        for index,value in enumerate(self._nArray):
            if(value == item):
                for jIdx in range(index,len(self._nArray)-1):
                    self._nArray[jIdx] = self._nArray[jIdx + 1]
                self._nASize -= 1
                return True # item deleted and array resized

        return False # item not found



    def search(self,item):
        for x in self._nArray:
            if(x == item):
                return True
        return False


    def traverse(self,function=print):
        for x in self._nArray:
            if(x != None):
                function(x)

