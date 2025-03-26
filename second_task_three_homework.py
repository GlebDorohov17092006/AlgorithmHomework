class Heap:
    def __init__(self) -> None:
        self.heap = []
        self.lenght = 0

    def siftDown(self, ind: int) -> None:
        if ((2*ind + 1) >= self.lenght):
            return
        child = 2*ind + 1
        if ((2*ind + 2)<self.lenght and self.heap[2*ind+2][1] < self.heap[child][1]):
            child = 2*ind + 2
        if self.heap[child][1] < self.heap[ind][1]:
            self.heap[child], self.heap[ind] = self.heap[ind], self.heap[child]
            self.siftDown(child)
        else:
            return  
        
        
    def siftUp(self, ind: int) -> None:
        if(ind==0):
            return 
        parent = (ind-1)//2
        if(self.heap[ind][1] < self.heap[parent][1]):
            self.heap[ind], self.heap[parent] = self.heap[parent], self.heap[ind]
            self.siftUp(parent)
        else:
            return
        
    def push(self, element: int) -> None:
        self.heap.append(element)
        self.lenght += 1
        self.siftUp(self.lenght - 1)

    def pop_min(self) -> None:
        buff = self.heap[0]
        self.heap[0], self.heap[self.lenght-1] = self.heap[self.lenght - 1], self.heap[0]
        self.lenght -= 1
        self.heap.pop()
        self.siftDown(0)
        return buff
    
def dead_end(n: int, ma: list[list[int]]) -> int:
    if n==0:
        return 0
    heap_bus = Heap()
    buff = 1
    for i in range(n):
        if heap_bus.lenght==0:
            heap_bus.push(ma[i])
        else:
            while heap_bus.lenght and heap_bus.heap[0][1] < ma[i][0]:
                heap_bus.pop_min()
            heap_bus.push(ma[i])
            buff = max(buff, heap_bus.lenght)
    return buff

print(dead_end(1, [[10,20]]))
print(dead_end(2,[[10,20],[20,25]]))
print(dead_end(3, [[10,20],[20,25],[21,30]]))

