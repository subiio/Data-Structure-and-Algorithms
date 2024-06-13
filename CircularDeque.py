from ArrayQueue import ArrayQueue
class  CircularDeque(ArrayQueue):
    def __init__(self,capacity = 10):
        super().__init__(capacity)
    def addRear(self,item):
        return self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity)  % self.capacity
            return item
        else: pass
    def addFront(self,item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front -1 + self.capacity) % self.capacity
        else: pass
    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else: pass

# 미로 데이터에 쉼표 추가
maze = [
    [0,0,0,0,0,0],
    [1,1,0,1,1,0],
    [0,1,1,1,0,0],  
    [0,1,0,1,0,0],
    [0,1,0,1,1,1],
    [0,0,0,0,0,0]
]

# 시작점과 도착점 정의
start = (1,0)
finish = (4,5)

def maze_runner(maze, start, finish):
    mazeDeque = CircularDeque(100)
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    mazeDeque.addRear(start)  # 시작점 추가

    while not mazeDeque.isEmpty():
        print(mazeDeque.array)
        current = mazeDeque.deleteFront()
        if current == finish:
            return True  # 도착점에 도달
        for d in direction:
            next_pos = (current[0] + d[0], current[1] + d[1])
            # 범위 검사 및 경로 가능 여부 검사
            if 0 <= next_pos[0] < len(maze) and 0 <= next_pos[1] < len(maze[0]) and maze[next_pos[0]][next_pos[1]] == 1:
                maze[next_pos[0]][next_pos[1]] = -1  # 방문 표시
                mazeDeque.addRear(next_pos)

    return False  # 도착점에 도달하지 못함
   
print(maze_runner(maze,start,finish))
# CircularDeque 및 ArrayQueue 구현은 이전 코드를 그대로 사용합니다.

            
            
            
            
            
            
    