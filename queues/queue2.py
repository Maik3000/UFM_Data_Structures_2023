
class Search:
    def search(key, arr):
        for i in range(len(arr)):
            if arr[i] == key:
                return i
        return -1  

    def peek(index, arr):
        if index >= len(arr):
            return None  
        return arr[index]


'''    
class CircularQueue:
    def __init__(self, k: int):
        self.k = k  
        self.queue = [None] * k  
        self.head = -1  
        self.tail = -1  

    def enqueue(self, item: int) -> bool:
        if self.is_full():  
            return False
        elif self.is_empty():  
            self.head, self.tail = 0, 0
        else:
            self.tail = (self.tail + 1) % self.k  
        self.queue[self.tail] = item  
        return True

    def dequeue(self) -> bool:
        if self.is_empty():  
            return False
        elif self.head == self.tail:  
            self.head, self.tail = -1, -1
        else:
            self.head = (self.head + 1) % self.k  
        return True

    def front(self) -> int:
        if self.is_empty():  
            return -1
        return self.queue[self.head]

    def rear(self) -> int:
        if self.is_empty():  
            return -1
        return self.queue[self.tail]

    def is_empty(self) -> bool:
        return self.head == -1

    def is_full(self) -> bool:
        return (self.tail + 1) % self.k == self.head
    
    #implementamos la operacion search
    def search(self, item: int) -> bool:
        if self.is_empty():  
            return False
        i = self.head
        while i != self.tail:
            if self.queue[i] == item:
                return True
            i = (i + 1) % self.k
        if self.queue[self.tail] == item:  
            return True
        return False
    
    #implementamos la operacion peek
    def peek(self) -> int:
        if self.is_empty():  
            return -1
        return self.queue[self.head]
'''