"""
Linked List - collection of Nodes
Head - First node of a linked list
Tail - Last node of a linked list, always points to None 
"""

#Node Defintion 
class Node:
    #Node - pointer and value
    def __init__(self,value):
        self.value = value 
        #point to next node
        self.next = None 

#Linked List Defintion 
class LinkedList:
    def __init__(self,value):
        #node creation
        new_node = Node(value)
        #assign head,tail,length
        self.head = new_node 
        self.tail = new_node 
        self.length = 1

    def print_list(self):
        #assign temp variable to store head value 
        temp = self.head
        #traverse till tail node 
        while temp is not None:
            #print temp value 
            print(temp.value)
            #get next node value 
            temp = temp.next

    def append(self,value):
        #create node 
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            #point current tail to new node 
            self.tail.next = new_node 
            #assign new node as tail node 
            self.tail = new_node
            #update list length 
            self.length += 1
   
new_linked_list = LinkedList(1)
# print(new_linked_list.head.value)
new_linked_list.append(2)
new_linked_list.print_list()

