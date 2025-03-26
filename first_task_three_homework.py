class Heap:
    def __init__(self):
        self.heap = []
        self.lenght = 0

    def siftDown(self, ind: int) -> None:
        if ((2*ind + 1) >= self.lenght):
            return
        child = 2*ind + 1
        if ((2*ind + 2)<self.lenght and self.heap[2*ind+2] < self.heap[child]):
            child = 2*ind + 2
        if self.heap[child] < self.heap[ind]:
            self.heap[child], self.heap[ind] = self.heap[ind], self.heap[child]
            self.siftDown(child)
        else:
            return  
        
        
    def siftUp(self, ind: int) -> None:
        if(ind==0):
            return 
        parent = (ind-1)//2
        if(self.heap[ind] < self.heap[parent]):
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

def min_sum(n: int, ma: list[int]) -> int:
    if n<=2:
        return sum(ma)
    heap_number = Heap()
    for i in range(n):
        heap_number.push(ma[i])
    su = 0
    while heap_number.lenght>2:
        mi1 = heap_number.pop_min()
        mi2 = heap_number.pop_min()
        su+=mi1 + mi2
        heap_number.push(mi1 + mi2)
    return su + heap_number.heap[0] + heap_number.heap[1]

print(min_sum(3,[1,2,3]))
print(min_sum(5,[5,2,3,4,6]))
print(min_sum(5,[3,7,6,1,9]))