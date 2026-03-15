import random
import matplotlib.pyplot as plt
from timeit import timeit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        if (self.head == None):
            element_one = Node(data)
            self.head = element_one
        else:
            element = Node(data)
            element.next = self.head
            self.head = element
        return
    
    def pop(self):
        if (self.head == None):
            return None
        else:
            wanted = self.head
            self.head = self.head.next
            return wanted.data


class StackArray:
    def __init__(self):
        self.data = []
    
    def push(self, data):
        self.data.append(data)
        

    def pop(self):
        if (len(self.data) == 0):
            return None
        return self.data.pop()
    
class StackDynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [] * self.capacity

    def push(self, data):
        if (data == None):
            return
        self.size += 1
        new_stack = [None] * self.size
        
        for i in range(0, self.size-1):
            new_stack[i] = self.data[i]
        new_stack[-1] = data

        self.data = new_stack
    
    def pop(self):
        if (self.size == 0):
            return None
        self.size -= 1
        new_stack = [None] * self.size

        for i in range(0, self.size-1):
            new_stack[i] = self.data[i]
        
        element = self.data[self.capacity-1]
        self.data = new_stack

        return element

        

    
def random_task(n):
    choice = ["push","pop"]
    probability = [0.7, 0.3]
    task = random.choices(choice, weights=probability, k=n)
    return task

def measure(tasks, stack):
    stack_time = 0
    for task in tasks:
        if task == "push":
            data = random.randint(0,1000)
            stack_time += timeit(lambda: stack.push(data), number=1)
        else:
            stack_time += timeit(lambda: stack.pop(), number=1)

    return stack_time

def main():
    stack_list = []
    stack_array_python = []

    for _ in range(100):
        tasks = random_task(10000)
        linked_list = StackLinkedList()
        array = StackArray()

        stack_list.append(measure(tasks, linked_list))
        stack_array_python.append(measure(tasks, array))
    
    plt.figure()
    plt.hist(stack_array_python, bins=20, alpha=0.5, label="Stack Array using python implemenation")
    plt.hist(stack_list, bins=20, alpha=0.5, label="Stack Linked List")
    plt.title("Comparing Stack Array vs Stack Linked List")
    plt.xlabel("Execution Time")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


def side():
    stack_array = []
    stack_list = []

    for _ in range(100):
        tasks = random_task(10000)
        dynamicArray = StackDynamicArray()
        linked_list = StackLinkedList()


        stack_array.append(measure(tasks, dynamicArray))
        stack_list.append(measure(tasks, linked_list))

    
    plt.figure()
    plt.hist(stack_array, bins=20, alpha=0.5, label="Stack Array using manual implemenation")
    plt.hist(stack_list, bins=20, alpha=0.5, label="Stack Linked List")
    plt.title("Comparing Stack Array vs Stack Linked List")
    plt.xlabel("Execution Time")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

if (__name__ == '__main__'):
    main()
    # side()

''' # Question 5
The results indicate that a stack array implementation is more efficient than a stack linked list. This is due to a 
couple of reasons. Python lists are implemented dynamically in a really efficient way using optimized C code, making
append() and pop() very efficient. To observe the difference I implemented my own dynamic arrays and seeing how much
worse the execution time is. You can see the results by uncommenting side(). The list implementation also requires a
new node object to be created each time and pointer reassignment with push() and pop(). This means that the array 
implementation should have faster execution times.

'''     
    