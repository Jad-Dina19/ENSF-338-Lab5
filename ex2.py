import random
from timeit import timeit
import matplotlib.pyplot as plt

class PriorityQueue1:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)
        self.merge_sort(0, len(self.data) - 1)

    def dequeue(self):
        if (len(self.data) == 0):
            return None
        return self.data.pop(0)
    
    def merge(self, low, mid, high):
        i = low
        j = mid + 1
        temp = []

        while (i <= mid and j <= high):
            if(self.data[i] <= self.data[j]):
                temp.append(self.data[i])
                i+=1
            else:
                temp.append(self.data[j])
                j+=1
    
        while (i <= mid):
            temp.append(self.data[i])
            i+=1
        while (j <= high):
            temp.append(self.data[j])
            j+=1

        for k in range(len(temp)):
            self.data[low + k] = temp[k]

    def merge_sort(self, low, high):
        if(low < high):
            mid = (low+high)//2
            self.merge_sort(low, mid)
            self.merge_sort(mid+1, high)
            self.merge(low, mid, high)

class PriorityQueue2:
    def __init__(self):
        self.data = []
    
    def enqueue(self, data):
        index = 0

        while (index < len(self.data) and data < self.data[index]):
            index += 1

        self.data.insert(index, data)
        

    def dequeue(self):
        if (len(self.data) == 0):
            return None
        return self.data.pop(0)


def random_task(n):
    choice = ["enqueue","dequeue"]
    probability = [0.7, 0.3]
    task = random.choices(choice, weights=probability, k=n)
    return task

def measure(tasks, queue):
    queue_time = 0
    for task in tasks:
        if task == "enqueue":
            data = random.randint(0,1000)
            queue_time += timeit(lambda: queue.enqueue(data), number=1)
        else:
            queue_time += timeit(lambda: queue.dequeue(), number=1)

    return queue_time


def main():
    queue1_time = []
    queue2_time = []
    for _ in range(100):
        task = random_task(1000)
        queue1 = PriorityQueue1()
        queue2 = PriorityQueue2()

        queue1_time.append(measure(task, queue1))
        queue2_time.append(measure(task, queue2))
    
    print("Queue 1 Times: " + queue1_time)
    print("Queue 2 Times: " + queue2_time)


    plt.figure()
    plt.hist(queue1_time, alpha=0.5, label="PriorityQueue1")
    plt.hist(queue2_time, alpha=0.5, label="PriorityQueue2")

    plt.xlabel("Execution Time")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
