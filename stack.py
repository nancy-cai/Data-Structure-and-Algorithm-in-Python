class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def is_empty(self):
        return self.items == []
        
    def top_item(self):
        if not self.is_empty:
            return self.items[-1]
        
    def get_stack(self):
        return self.items
 
        
def string_reverser_stack(stack, strr):
    # Loop through the letters and push them to the stack one by one
    for i in range(len(strr)):
        stack.push(strr[i])
    
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
        
    return reversed_str
    
stack = Stack()
strr = 'meow meow'
print(string_reverser_stack(stack, strr))
        