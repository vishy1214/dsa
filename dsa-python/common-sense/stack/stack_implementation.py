
class Stack:
     #LIFO
    __stack_array__ = []

    def pop(self):
        if(self.size() > 0):
            self.__stack_array__.remove(self.__stack_array__[self.size()-1])

    def push(self,element):
        self.__stack_array__.append(element)
    def head(self):
        if(self.size() > 0):
            return self.__stack_array__[self.size()-1]
        else:
            return None
    def size(self):
         return len(self.__stack_array__)

    def clear_stack(self):
        self.__stack_array__.clear()
