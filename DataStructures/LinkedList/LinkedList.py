from Node import *

class LinkedList:
    def __init__(self, arr):
        self.head = None

        for i in range(len(arr)): 
            if i == 0:
                self.head = Node(i)
            
            else: 
                self.insert(self.head, arr[i])


    def insert(self, root, data):

        print('root.value', root.value)
        print('root.next', root.next)
        print('data', data)

        print('----------------------------------------------------------')

        if root.next is None:
            root.next == Node(data)

            print('root.value', root.value)
            print('root.next', root.next)
            print('data', data)

        else:
            self.insert(root.next, data)

    def remove(self, value):
        pass

    def printLinkedList(self, root):
        if root.next is None:
            return 
        
        else:
            print(root.value)
            self.printLinkedList(root.next)

    def reverseLinkedList(self, root):
        pass

    def LinkedList2Arr(self, root):
        pass