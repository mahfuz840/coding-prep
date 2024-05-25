class QueueWithTwoStack:

    def __init__(self):
        self.arr1 = []
        self.arr2 = []

    def enqueue(self, num: int):
        self.arr1.append(num)

    def dequeue(self):
        if self.isEmpty():
            raise Exception('already empty')

        while len(self.arr1):
            self.arr2.append(self.arr1.pop())
        
        value = self.arr2.pop()

        while len(self.arr2):
            self.arr1.append(self.arr2.pop())
        
        return value

    def isEmpty(self):
        return len(self.arr1) == 0


q = QueueWithTwoStack()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())
# print(q.dequeue())
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())