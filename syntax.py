"""
commented syntax for various data structures and algorithms
"""


### STACK (LIFO)  ###

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""

class Stack:
    def __init__(self): #constructor for the object we are creating (stacks are the object)
        self.items = []  #creates items property for the created object

    def is_empty(self):
        #return len(self.items) == 0 #check if empty (non pythonic way)
        return not self.items

    def push(self, item):       #adds to the end of a stack
        self.items.append(item)

    def pop(self):                  #returns last element and removes it
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()
    s.push("d")
    s.push("i")
    s.push("c")
    s.push("k")
    s.pop()
    print(s)

"""if __name__ == "__main__":
    s = Stack()
    for char in string:
        s.push(char)
    while not (s.is_empty()):
        reversed_string += s.pop()

    print(reversed_string)"""


### QUEUE (FIFO)  ###

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    q.dequeue()
    print(q.size())
    print(q.peek())
    print(q)

### PRIORITY QUEUE ###
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority,item))

    def get(self):
        return heapq.heappop(self.elemnts)[1]

    def __str__(self):
        return str(self.elements)



#LINKED LIST

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__=='__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second;
    second.next = third;

llist.printList()


