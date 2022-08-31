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

    def prepend(self,value):
        #create node
        new_node = Node(value)
        #point new node to existing head 
        new_node.next = self.head 
        #assign new node as head node 
        self.head = new_node 
    
    def pop(self):
        #temp - holds current node
        #pre - holds previous node 
        temp = self.head
        pre = self.head 
        #traverse till next is not none
        while temp.next is not None:
            pre = temp 
            temp = temp.next
        #assign pre node as tail node 
        self.tail = pre 
        #assign next as None for tail node
        self.tail.next = None 
        return temp 

    def popfirst(self):
        temp = self.head
        #assign next node of head as head node 
        self.head = self.head.next 
        #update next value for old head
        temp.next = None
        #update list length 
        self.length -= 1
        return temp 

    def get(self,index):
        if index < 0 or index >= self.length:
            return None 
        else:
            temp = self.head 
            for _ in range(index):
                temp = temp.next
            return temp.value #for get
            #return temp - for set 

    def set_value(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value 
            return True 
        return False
            
                

new_linked_list = LinkedList(1)
# print(new_linked_list.head.value)
new_linked_list.append(2)
new_linked_list.prepend(0)
# new_linked_list.pop()
# new_linked_list.popfirst()
print(new_linked_list.get(0))
new_linked_list.set_value(0,5)
new_linked_list.print_list()

