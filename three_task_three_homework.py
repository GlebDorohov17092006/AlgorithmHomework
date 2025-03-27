class Heap:
    def __init__(self):
        self.heap = []
        self.lenght = 0

    def siftDown(self, ind: int) -> None:
        if ((2*ind + 1) >= self.lenght):
            return
        child = 2*ind + 1
        if ((2*ind + 2)<self.lenght and self.heap[2*ind+2][0] > self.heap[child][0]):
            child = 2*ind + 2
        if self.heap[child][0] > self.heap[ind][0]:
            self.heap[child], self.heap[ind] = self.heap[ind], self.heap[child]
            self.siftDown(child)
        else:
            return  
        
        
    def siftUp(self, ind: int) -> None:
        if(ind==0):
            return 
        parent = (ind-1)//2
        if(self.heap[ind][0] > self.heap[parent][0]):
            self.heap[ind], self.heap[parent] = self.heap[parent], self.heap[ind]
            self.siftUp(parent)
        else:
            return
        
    def push(self, element: list[list[int]]) -> None:
        self.heap.append(element)
        self.lenght += 1
        self.siftUp(self.lenght - 1)

    def pop_max(self) -> list[int]:
        buff = self.heap[0]
        self.heap[0], self.heap[self.lenght-1] = self.heap[self.lenght - 1], self.heap[0]
        self.lenght -= 1
        self.heap.pop()
        self.siftDown(0)
        return buff

def windows(n:int, k: int, ma: list[int]) -> list[int]:
    heap_window = Heap()
    answer = []
    for i in range(n):
        heap_window.push([ma[i],i])
        while heap_window.heap[0][1] < (i - k + 1):
            heap_window.pop_max()
        if i >= (k - 1):
            answer.append(heap_window.heap[0][0])
    return answer

print(windows(9, 4, [20, 27, 3, 8, 4, 5, 10, 4, 6]))


