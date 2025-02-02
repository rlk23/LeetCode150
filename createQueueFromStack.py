'''
mplement a queue using the stack data structure. Include the following functions:

enqueue(x: int) -> None: adds x to the end of the queue.
dequeue() -> int: removes and returns the element from the front of the queue.
peek() -> int: returns the front element of the queue.
You may not use any other data structures to implement the queue.

Example
Input: [enqueue(1), enqueue(2), dequeue(), enqueue(3), peek()]
Output: [1, 2]
Constraints:
The dequeue and peek operations will only be called on a non-empty queue.

'''

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        if self.queue:
            val = self.queue.pop(0)
            return val

    def peek(self) -> int:
        if self.queue:
            return self.queue[0]
