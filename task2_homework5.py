class Heap:
    def __init__(self):
        self.heap = []
        self.lenght = 0

    def siftDown(self, ind: int) -> None:
        if ((2*ind + 1) >= self.lenght):
            return
        child = 2*ind + 1
        if ((2*ind + 2)<self.lenght and self.heap[2*ind+2] > self.heap[child]):
            child = 2*ind + 2
        if self.heap[child] > self.heap[ind]:
            self.heap[child], self.heap[ind] = self.heap[ind], self.heap[child]
            self.siftDown(child)
        else:
            return  
        
        
    def siftUp(self, ind: int) -> None:
        if(ind==0):
            return 
        parent = (ind-1)//2
        if(self.heap[ind] > self.heap[parent]):
            self.heap[ind], self.heap[parent] = self.heap[parent], self.heap[ind]
            self.siftUp(parent)
        else:
            return
        
    def push(self, element: int) -> None:
        self.heap.append(element)
        self.lenght += 1
        self.siftUp(self.lenght - 1)

    def pop_max(self) -> None:
        buff = self.heap[0]
        self.heap[0], self.heap[self.lenght-1] = self.heap[self.lenght - 1], self.heap[0]
        self.lenght -= 1
        self.heap.pop()
        self.siftDown(0)
        return buff
n, k = map(int, input().split())
ma = Heap()
for element in input().split():
    if ma.lenght < k:
        ma.push(int(element))
    else:
        ma.push(int(element))
        ma.pop_max()
print(*sorted(ma.heap))



