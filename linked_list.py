# implementing linked list data structure 
# linked list are data records linked together via pointers 
# there are two different types of linked list namely
# -- singly linked list : each pointer refers to the next element in the list
# -- doubly linked list : ecah pointer refers to next and previous element in the list

class SinglyLLNode:
    """
    A node in our linked list
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return repr(self.data)

class SinglyLinkedList:
    def __init__(self):
        """ 
        initialize the linked list with a head
        """
        self.head = None

    def prepend(self, data):
        """
        place the node as the head of the linked list 
        """
        self.head = SinglyLLNode(data=data , next=self.head)
        

    def append(self, data):
        """
        inserting the element at the end of the list
        if head is not present then we want to insert the
        element at the head . 
        else we have to iterate till the end and append the element
        in he end
        """
        if not self.head :
            self.head = SinglyLLNode(data = data, next = None)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = SinglyLLNode(data = data ,next = None)
        return current.next

    def search(self, element):
        """
        iterate over the list and while iterating compare each node 
        with the element 
        """
        current = self.head
        while current and current.data != element:
            current = current.next
        return current

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'
    
    def remove(self , element):
        """
        find the element and keep a reference to the 
        element preceeding it . Unlink the element from the list 
        by updating the link of the previous node 
        """
        current = self.head 
        previous = None

        while current and current.data != element:
            previous = current
            current = current.next

        if previous == None :
            self.head = current.next
        elif current :
            previous.next = current.next
            current.next = None





class DoublyLLNode():
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next 
        self.previous = previous
    def __repr__(self):
        return repr(self.data)

class DoublyLinkedList:
    def __init__(self):
        # create a doubly linked list with the head initailize
        self.head = None

    def __repr__(self):
        nodes = []
        
        if self.head is None :
            print( "no element in the list" )
            return

        current = self.head
        
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self ,data):
        """
        inserting a new element at the begining of the list
        """
        new_head = DoublyLLNode(data = data, next = self.head)
        if self.head:
            self.head.prev = new_head
        self.head =  new_head

    def append(self, data):
        """
        insert the new element at the end of the list
        """
        if not self.head :
            new_element = DoublyLLNode(data = data)
            self.head = new_element
            return 
        current = self.head
        while current.next is not None:
            current = current.next
        new_node = DoublyLLNode(data = data)
        current.next = new_node
        new_node.previous = current
    
    def delete_by_value (self , value):
        if self.head == None :
            print("no element found")
            return
        if self.head.next is None :
            if self.head.data == data :
                self.head = None 
            else :
                print ("item not found")
            return

        if self.head.data == value:
            self.head = self.head.next
            self.head.previous = None
            return
        
        current = self.head
        while current.next is not None:
            if current.data == value:
                break
            current = current.next
        if current.next is not None:
            current.previous.next = current.next
            current.next.previous = current.previous
        else:
            if current.data == value:
                current.previous.next = None
            else :
                print('element not find stupid')



