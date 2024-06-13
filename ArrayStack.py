class ArrayStack:
    def __init__(self,capacity):
        self.array = [None]*capacity
        self.capacity = capacity
        self.top  = -1
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return  self.top == self.capacity -1
    def push(self,element):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = element
        else:
            print("Stack overflow")
            exit()
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:
            print("Stack underflow")
            exit()
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("Stack underflow")
            exit()
    def size(self):
        return self.top + 1
    def find_max(self):
        tmp = 0
        for i in range(self.top + 1):
            if self.array[i] > tmp:
                tmp = self.array[i]
        return tmp

   
# 1.1 말을 거꾸로 뒤집는 예제
# s = ArrayStack(100)
# msg = input("문자열 입력: ")
# for c in msg:
#     s.push(c)
# while not s.isEmpty():
#     print(s.pop(),end = '')
# print()


# 1.2 find_max 함수 예제
# s = ArrayStack(5)
# for i in range(5):
#     s.push(i)
# print(s.find_max())


# 1.3 
# def checkBrackets(statement):
#     stack = ArrayStack(100)
#     for ch in statement:
#         if ch in ('{','[','('):
#             stack.push(ch)
#         elif ch in ('}',']',')'):
#             if stack.isEmpty():
#                 return False
#             else:
#                 left = stack.pop()
#                 if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch == ")" and left != "("):
#                     return False
#                 else:
#                     stack.push(ch)
#     return stack.array

# print(checkBrackets('sex{machine}{}{}{}{}{}{}()()()[][][]'))



# 1.4 팩토리얼
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# 1.5 
# def hanoi_tower(n,fr,tmp,to):
#     count = 0
#     if (n == 1):
#         print("원판 1: %s --> %s" %(fr,to))
#     else:
#         hanoi_tower(n-1,fr,to,tmp)
#         print("원판 %d: %s --> %s" %(n,fr,to))
#         hanoi_tower(n-1,tmp,fr,to)
# hanoi_tower(5,'A','B','C')



# 1.6 후위수식
# def calcPostfixExpr(expr):
#     s = ArrayStack(100)
#     for a in expr:
#         if a in ('*','/','+','-'):
#             second = s.pop()
#             first = s.pop()
#             if a == '+':
#                 temp = first + second
#             elif a == '-':
#                 temp = first - second
#             elif a == '*':
#                 temp = first * second
#             elif a == '/':
#                 temp = first/ second
#             s.push(temp)
#         else:
#             s.push(int(a))
#     result = s.pop
#     return result             
# expr = "23*54*+9-"
# print(calcPostfixExpr(expr))

# 1.7 미로 탐색 알고리즘
# def searchExit(maze, entrance, exit):
#     s = ArrayStack(100)  # 스택 s 초기화
#     s.push(entrance)  # 입구의 위치를 스택에 삽입
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 위, 아래, 오른쪽, 왼쪽 이동
#     while s.isEmpty():  # 스택이 비어있지 않는 동안
#         current_position = s.pop()  # 현재 위치
#         if current_position == exit:  # 현재 위치가 출구 위치이면
#             return True  # 성공
#         x, y = current_position
#         maze[x][y] = 2  # 현재 위치를 방문했다고 표시 (미로에서 0: 갈 수 있는 길, 1: 벽, 2: 방문한 길)
#         for dx, dy in directions:  # 모든 방향에 대해서
#             nx, ny = x + dx, y + dy
#             # 미로 범위 내이고, 방문하지 않았으며, 갈 수 있는 길이면
#             if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
#                 s.push((nx, ny))  # 그 위치를 스택에 push
#     return False  # 실패

# def searchExit(maze,entrance,exit):
#     s = ArrayStack(100)
#     s.push(entrance)
#     direction = [(0,1),(0,-1),(1,0),(-1,0)]
#     path = []
#     while not s.isEmpty():
#         current_position = s.pop()
#         x,y = current_position
#         if maze[x][y] == 2:
#             continue
#         path.append(current_position)
#         if current_position == exit:
#             return path
#         maze[x][y] = 2
#         for dx, dy in direction:
#             nx, ny = x+dx, x+dy
#             if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
#                 s.push((nx,ny))
#     return False
    


def searchExit(maze,entrance,exit):
    s = ArrayStack(100)
    s.push(entrance)
    path  =[]
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while not s.isEmpty():
        current_path = s.pop()
        x,y = current_path
        if maze[x][y] == 2:
            continue
        path.append(current_path)
        if current_path == exit:
            return path
        maze[x][y] =2
        for dx, dy in direction:
            nx,ny = x+dx, y+dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze) and maze[nx][ny] == 0:
                s.push((nx,ny))
    return False

def searchExit(maze,entrance,exit):
    s = ArrayStack(100)
    s.push(entrance)
    path = []
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    while not s.isEmpty():
        current_path = s.pop()
        x,y = current_path
        if maze[x][y] == 2:
            continue
        path.append(current_path)
        if current_path == exit:
            return path
        maze[x][y] = 2    
        for dx,dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(maze) and  0 <= ny < len(maze) and maze[nx][ny] == 0:
                s.push((nx,ny))
    return False

    



# def searchExit(maze, entrance, exit):
#     s = ArrayStack(100)  # 스택 s 초기화= 
#     s.push(entrance)  # 입구의 위치를 스택에 삽입
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 위, 아래, 오른쪽, 왼쪽 이동
#     path = []  # 쥐가 이동한 경로를 저장할 리스트
#     while not s.isEmpty():  # 스택이 비어있지 않는 동안
#         current_position = s.pop()  # 현재 위치
#         x, y = current_position
#         if maze[x][y] == 2:  # 이미 방문한 위치면 무시 (백트래킹 방지)
#             continue
#         path.append(current_position)  # 경로에 현재 위치 추가
#         if current_position == exit:  # 현재 위치가 출구 위치이면
#             return path  # 경로 반환
#         maze[x][y] = 2  # 현재 위치를 방문했다고 표시 (미로에서 0: 갈 수 있는 길, 1: 벽, 2: 방문한 길)
#         for dx, dy in directions:  # 모든 방향에 대해서
#             nx, ny = x + dx, y + dy
#             # 미로 범위 내이고, 방문하지 않았으며, 갈 수 있는 길이면
#             if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
#                 s.push((nx, ny))  # 그 위치를 스택에 push
#     return False  # 실패

# # 미로 탐색 실행
# path = searchExit(maze, entrance, finish)
# if path:
#     for p in path:
#         print(p)
# else:
#     print("출구를 찾을 수 없습니다.")

