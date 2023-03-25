#----------------------------------------------------
# Stack implementation
#----------------------------------------------------

class Stack:
    '''
    An object in this class represents a single stack
    '''    
    def __init__(self):
        '''
        initialize the empty list
        '''
        self.items = []                                
    
    def push(self, item):
        '''
        append the item in the list
        '''
        self.items.append(item)                         # add the item to last index of a list

    
    #RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self): 
        '''
        pop the last element of the list
        '''
        try:
            return self.items.pop()                     #removes the last element of the list
        except:
            raise Exception('Stack is empty')

    
    #RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self): 
        '''
        returns the first element of the list
        '''
        try:
            return self.items[len(self.items)-1]        #returns the last element in the list
        except:
            raise Exception("Stack is empty")
    
    def isEmpty(self):
        '''
        check whether the list is empty or not
        '''
        return self.items == []
    
    def size(self):
        '''
        returns the size of the list
        '''
        return len(self.items)
    
    def show(self):
        '''
        prints the list
        '''
        print(self.items)
    
    def __str__(self):
        '''
        prints the list in string format
        '''
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        '''
        clear the list
        '''
        if self.items != []:
            self.items = []    