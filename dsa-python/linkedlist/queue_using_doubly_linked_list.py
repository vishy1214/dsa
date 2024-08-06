
#
Algorithm







class Node:
    head_ptr=None
    data = None
    tail_ptr=None

    def __init__(self,data):
        self.data = data
        return self


class Q:
    __first_node = None
    __last_node = None

    def __init__(self): 
        self.__first_node = None
        self.__last_node = None

    #Insert new item to the Q at the last
    def enQueue(self,data):
        if(self.__first_node.data == None and self.__first_node.tail_ptr == None):
            self.__first_node.data = data
        elif(self.__last_node == None):
            next_node = Node(data)
            next_node.head_ptr = self.__first_node
            self.__last_node = next_node
            self.__first_node.tail_ptr = self.__last_node
        else:
            next_node = Node(data)
            self.__last_node.tail_ptr = next_node
            next_node.head_ptr = self.__last_node
            self.__last_node = next_node

