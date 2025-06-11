#/**********************************************************  
# Name: armaan salman                   CSC 242  
#* Date: 2/23/25                Lab 3  
#**********************************************************  
#* Statement:  this program is to implement a stack using a linked list. the files allow for stack operations such as push and pop.
#* 
#* Specifications:  
#* - elements are added and removed.
#* - last in first out method
#*  
#* Input - there is no input that user is prompted to put
#*  
#* Output - output is the stack, the top element and the size of the stack
#**********************************************************/



from myLinkedList import MyLinkedList

class MyStack(MyLinkedList):

    def __init__(self):
        super().__init__()

    # Returns the string representation of the linked list.
    def __str__(self):
        if self.size == 0:
            return "...EMPTY STACK...count = 0"

        current = self.first
        result = []
        while current:
            result.append(str(current.data))
            current = current.next

        return "\n".join(result)

    # returns the top element of the stack
    # Postcondition: Assuming the stack is not empty, the top element
    # of the stack is returned, else return false
    def getTop(self):
        return self.getFirst() if self.size > 0 else False

    # adds a new item to the stack
    # Postcondition: The parameter theItem is added to the top of the stack
    def push(self, theItem):
        self.addFirst(theItem)

    # Returns the number of items in the stack
    def getCount(self):
        return self.size

    # removes the top element of the stack
    # Precondition: the stack is not empty
    # Postcondition: the top element of the stack is removed from stack and the 
    # size is decremented by 1
    def pop(self):
        if self.size == 0:
            return False

        popped_item = self.first.data
        self.first = self.first.next
        self.size -= 1

        if self.size == 0:
            self.last = None

        return popped_item
