class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.head.data
        self.head = self.head.next
        self._size -= 1
        if self.head is None:
            self.tail = None
        return item

    def first(self):
        if self.is_empty():
            return None
        return self.head.data

    def __len__(self):
        return self._size

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "head [ " + " -> ".join(elements) + " ] tail"

if __name__ == "__main__":
    cola = LinkedQueue()
    cola.enqueue("A")
    cola.enqueue("B")
    cola.enqueue("C")
    print(cola)
    print(cola.dequeue())
    print(cola)