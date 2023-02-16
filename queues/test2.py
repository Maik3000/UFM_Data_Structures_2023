
from queue2 import Search
#test search
numbers = [1, 3, 5, 7, 9, 11]
test = search(2, numbers)
print(test)

#test peek
numbers = [1, 3, 5, 7, 9, 11]
index = peek(5, numbers)
next_element = peek(index + 1, numbers)
print(next_element)
'''

from queue2 import CircularQueue
q = CircularQueue(5)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.is_empty()

print(q.enqueue(6))  

print(q.dequeue())  
print(q.dequeue())  

q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.front() == 3

q.peek() == 4
q.dequeue() 
q.peek() == 5
q.dequeue()
q.peek() == 6
q.dequeue()
q.peek() == 1
print(q.dequeue())  

print(q.is_empty())
print(q.dequeue())
'''