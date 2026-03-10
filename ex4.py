import sys
import random
from timeit import timeit
import matplotlib.pyplot as plt

class ArrayQueue:
    def __init__(self):
        self.queue = []
        self.size = 0
   

    def enqueue(self, value):
        if(value == None):
            return
        self.size +=1
        new_queue = [None] * self.size
        new_queue[0] = value
        for i in range(1, self.size):
            new_queue[i] = self.queue[i-1]
        
        self.queue = new_queue


    def dequeue(self):
        if self.size == 0:
            return None

        rem = self.queue[self.size - 1]
        self.queue[self.size - 1] = None
        self.size -= 1
        return rem


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, node):
        self.next = node
    
    def get_next(self):
        return self.next
       
class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        node = Node(value)
        
        if(node == None):
            raise ValueError("Node must not be none")
        
        if(self.head == None):
            self.head = node
            self.tail = node
            return
        
        successor = self.head
        self.head = node
        node.set_next(successor)

    def dequeue(self):
        if(self.head == None):
            return 
        if(self.head == self.tail):
            current = self.tail
            self.tail = None
            self.head = None
            return current.data


        current = self.head
        while(current.get_next() != self.tail):
            current = current.get_next()

        rem = self.tail
        current.set_next(None)
        self.tail = current
        return rem.data

        
def generate_tasks():
    tasks = []
    for i in range(10000):
        if random.random() < 0.7:
            tasks.append("enqueue")
        else:
            tasks.append("dequeue")
    return tasks

def run_task(task, queue):
    for x in task:
        if(x == "enqueue"):
            queue.enqueue(0)
        else:
            queue.dequeue()

def plot_distribution(arr_times, ll_times):
    plt.hist(arr_times, bins= 20, alpha=0.5, label="ArrayQueue")
    plt.hist(ll_times, bins=20, alpha=0.5, label="LLQueue")
    plt.xlabel("time")
    plt.ylabel("frequency")
    plt.legend()
    plt.show()

def main():
    ll_times = []
    arr_times = []
    for i in range(100):
        task = generate_tasks()
        queue_ll = LLQueue()
        queue_arr = ArrayQueue()
        ll_times.append(timeit(lambda: run_task(task, queue_ll), number=1))
        arr_times.append(timeit(lambda: run_task(task, queue_arr), number=1))
        

    print("Array Times:", arr_times)  
    print("LinkedList Times", ll_times)  

    plot_distribution(arr_times, ll_times)




if(__name__ == "__main__"):
    main()