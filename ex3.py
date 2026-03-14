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
    stack_array = []
    stack_list = []

    for _ in range(100):
        tasks = random_task(10000)
        array = StackArray()
        linked_list = StackLinkedList()

        stack_array.append(measure(tasks, array))
        stack_list.append(measure(tasks, linked_list))
    
    plt.figure()
    plt.hist(stack_array, alpha=0.5, label="Stack Array using python implemenation")
    plt.hist(stack_list, alpha=0.5, label="Stack Linked List")
    plt.title("Comparing Stack Array vs Stack Linked List")
    plt.xlabel("Execution Time")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()



if (__name__ == '__main__'):
    main()

            
    