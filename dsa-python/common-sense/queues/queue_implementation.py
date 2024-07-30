class Queue:
    __Q__ = []

    def clear(self):
        self.__Q__.clear()

    def enqueue(self,element):
        self.__Q__.append(element)

    def dqueue(self):
        self.__Q__.remove(self.__Q__[0])

    def size(self):
        return len(self.__Q__)

    def list_all(self):
        return self.__Q__


testingQ = Queue()
testingQ.enqueue(1)
testingQ.enqueue(2)
print(testingQ.list_all())
testingQ.dqueue()
testingQ.dqueue()
print(testingQ.list_all())
