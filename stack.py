''' Implementation of a Stack with python lists (arrays NOT linked lists) '''

'''
Stack is based on LIFO - Last in, First out
'''

class Stack:
    def __init__(self):
        '''
        Stacks Constructor
        Time Complexity: O(1) - we are making a fixed number of actions
        '''
        self.stack = []
        self.size = 0

    def is_empty(self):
        '''
        Checks whether the stack is empty
        Time Complexity: O(1) - we are making a fixed number of actions
        '''
        return self.size == 0


    def top(self):
        '''
        Returns the top element of the stack
        Time Complexity: O(1) - we are making a fixed number of actions
        '''
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self.stack[self.size-1]

    def push(self, data):
        '''
        Time Complexity: O(1) - we are making a fixed number of actions
        '''
        self.stack.append(data)
        self.size += 1

    def pop(self):
        '''
        Pops the top element
        Time Complexity: O(n) - because slicing takes a complexity of O(size of the list).
        '''
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return_val = self.stack[self.size-1]
            self.stack = self.stack[0:self.size-1]
            self.size -= 1
            return return_val

    def __repr__(self):
        '''
        String Representation of the stack
        Time Complexity: O(n) - because we are running on all the elements in the stack
        '''
        if self.is_empty():
            return '[]'
        s = 'stack: '
        for element in self.stack[::-1]:
            s += str(element) + ' -> '
        return s[:-3] + ' ,size: ' + str(self.size)


# my_stack = Stack()
# print(my_stack.stack)
# print(my_stack.size)
# print(my_stack.__repr__())
# my_stack.push('hey')
# my_stack.push('there')
# print(my_stack.stack)
# print(my_stack.size)
# print(my_stack.__repr__())





