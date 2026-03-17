class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def enqueue(self, element):
        if self.size == self.capacity:
            print("enqueue None")
            return None

        rear = (self.front + self.size) % self.capacity
        self.data[rear] = element
        self.size += 1
        print(f"enqueue {element}")
        return element

    def dequeue(self):
        if self.size == 0:
            print("dequeue None")
            return None

        element = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.size == 0:
            print("peek None")
            return None

        element = self.data[self.front]
        print(f"peek {element}")
        return element


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularQueueLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.tail = None  # tail.next is front

    def enqueue(self, element):
        if self.size == self.capacity:
            print("enqueue None")
            return None

        new_node = Node(element)

        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        print(f"enqueue {element}")
        return element

    def dequeue(self):
        if self.size == 0:
            print("dequeue None")
            return None

        front = self.tail.next
        element = front.value

        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = front.next

        self.size -= 1
        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.size == 0:
            print("peek None")
            return None

        element = self.tail.next.value
        print(f"peek {element}")
        return element


def get_test_operations(queue_name="MyList"):
    """
    so this returns 40 opera tions and their expected terminal output.
    these ops. test:
    - enqueue into empty queue
    - dequeue from empty queue
    - peek from empty queue
    - enqueue into full queue
    - normal FIFO behavior
    - wrap-around behavior
    """
    operations = [
        (f"{queue_name}.dequeue()", "dequeue None"),
        (f"{queue_name}.peek()", "peek None"),
        (f"{queue_name}.enqueue(10)", "enqueue 10"),
        (f"{queue_name}.peek()", "peek 10"),
        (f"{queue_name}.enqueue(20)", "enqueue 20"),
        (f"{queue_name}.enqueue(30)", "enqueue 30"),
        (f"{queue_name}.dequeue()", "dequeue 10"),
        (f"{queue_name}.peek()", "peek 20"),
        (f"{queue_name}.enqueue(40)", "enqueue 40"),
        (f"{queue_name}.enqueue(50)", "enqueue 50"),
        (f"{queue_name}.enqueue(60)", "enqueue 60"),
        (f"{queue_name}.enqueue(70)", "enqueue None"),
        (f"{queue_name}.dequeue()", "dequeue 20"),
        (f"{queue_name}.dequeue()", "dequeue 30"),
        (f"{queue_name}.enqueue(70)", "enqueue 70"),
        (f"{queue_name}.enqueue(80)", "enqueue 80"),
        (f"{queue_name}.peek()", "peek 40"),
        (f"{queue_name}.enqueue(90)", "enqueue None"),
        (f"{queue_name}.dequeue()", "dequeue 40"),
        (f"{queue_name}.dequeue()", "dequeue 50"),
        (f"{queue_name}.peek()", "peek 60"),
        (f"{queue_name}.enqueue(90)", "enqueue 90"),
        (f"{queue_name}.enqueue(100)", "enqueue 100"),
        (f"{queue_name}.dequeue()", "dequeue 60"),
        (f"{queue_name}.dequeue()", "dequeue 70"),
        (f"{queue_name}.dequeue()", "dequeue 80"),
        (f"{queue_name}.peek()", "peek 90"),
        (f"{queue_name}.dequeue()", "dequeue 90"),
        (f"{queue_name}.dequeue()", "dequeue 100"),
        (f"{queue_name}.dequeue()", "dequeue None"),
        (f"{queue_name}.peek()", "peek None"),
        (f"{queue_name}.enqueue(111)", "enqueue 111"),
        (f"{queue_name}.enqueue(222)", "enqueue 222"),
        (f"{queue_name}.peek()", "peek 111"),
        (f"{queue_name}.dequeue()", "dequeue 111"),
        (f"{queue_name}.enqueue(333)", "enqueue 333"),
        (f"{queue_name}.peek()", "peek 222"),
        (f"{queue_name}.dequeue()", "dequeue 222"),
        (f"{queue_name}.dequeue()", "dequeue 333"),
        (f"{queue_name}.peek()", "peek None"),
    ]
    return operations


def print_test_operations_and_expected_output(queue_name="MyList"):
    operations = get_test_operations(queue_name)

    print("40 test operations with expected output:\n")
    for i, (operation, expected) in enumerate(operations, start=1):
        print(f"{i:02d}. {operation:<20} -> {expected}")


def run_demo(queue_class, name):
    print(f"\n=== Testing {name} ===")
    q = queue_class(5)

    operations = [
        ("dequeue", None),
        ("peek", None),
        ("enqueue", 10),
        ("peek", None),
        ("enqueue", 20),
        ("enqueue", 30),
        ("dequeue", None),
        ("peek", None),
        ("enqueue", 40),
        ("enqueue", 50),
        ("enqueue", 60),
        ("enqueue", 70),
        ("dequeue", None),
        ("dequeue", None),
        ("enqueue", 70),
        ("enqueue", 80),
        ("peek", None),
        ("enqueue", 90),
        ("dequeue", None),
        ("dequeue", None),
        ("peek", None),
        ("enqueue", 90),
        ("enqueue", 100),
        ("dequeue", None),
        ("dequeue", None),
        ("dequeue", None),
        ("peek", None),
        ("dequeue", None),
        ("dequeue", None),
        ("dequeue", None),
        ("peek", None),
        ("enqueue", 111),
        ("enqueue", 222),
        ("peek", None),
        ("dequeue", None),
        ("enqueue", 333),
        ("peek", None),
        ("dequeue", None),
        ("dequeue", None),
        ("peek", None),
    ]

    for action, value in operations:
        if action == "enqueue":
            q.enqueue(value)
        elif action == "dequeue":
            q.dequeue()
        elif action == "peek":
            q.peek()


if __name__ == "__main__":
    # q3: print the required 40 test operations and expected output
    print_test_operations_and_expected_output("MyList")

    # js some demos showing that both implementations produce the expected terminal output
    run_demo(CircularQueueArray, "CircularQueueArray")
    run_demo(CircularQueueLinkedList, "CircularQueueLinkedList")
