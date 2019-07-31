class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur=cur.next
        
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ": "+ node.value)
        
    # A -> B -> C -> D -> 0
    # A <- B <- C <- D <- 0
    def reverse_iterative(self): # https://www.youtube.com/watch?v=xFuJI29BiDY
        prev = None
        cur = self.head
        
        while cur:
            nxt = cur.next # Save it to a temp var
            cur.next = prev # Flip the arrow to point to the prev node
            prev = cur # Move along the list still from left to right
            cur = nxt # Move along the list still from left to right
            self.print_helper(prev, "prev")
            self.print_helper(cur, "cur")
        self.head = prev # when cur is D, we flip the arrow, set prev to D and move to the next node which is None, exit loop. then set head to prev which is D
     
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur: # if cur reached end of the list(None), return prev. Otherwise keep going through the list and reverse it by calling this fun itself
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return  _reverse_recursive(cur, prev)
            
        self.head = _reverse_recursive(cur=self.head, prev=None)
            
llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.reverse_iterative()
llist.print_list()
            
            