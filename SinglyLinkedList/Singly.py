class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Singly:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start==None
    def insert_at_first(self, data):
        newNode = Node(data, self.start)
        self.start=newNode

    def insert_at_last(self, data):
        newNode = Node(data)
        if self.start != None:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        else:
            self.start = newNode

    def search(self, value):
        temp = self.start
        print("temp ", temp.item)
        while temp !=None:
            if temp.item == value:
                return temp
            temp = temp.next
        return None

    def insert_after(self, targetNode, data):
        newNode = Node(data)
        if targetNode != None and self.search(targetNode.item):
            temp = targetNode.next
            targetNode.next = newNode
            newNode.next = temp
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def delete(self):
        if self.start !=None:
            prev = Node

myList = Singly()

myList.insert_at_first(20)
myList.insert_at_first(22)
myList.insert_at_last(27)
print(myList.search(22).item)
myList.insert_after(myList.search(20),25)
myList.print_list()








