#Find short possible path in 2d, from top lef to bottom right, can be optimizet if have walls
from collections import deque
grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

Y, X = len(grid), len(grid[0])
moves = [(0,1),(1,0)]
visited = set()
Q = deque()

Q.append((1,(0,0)))
visited.add((0,0))

while Q:
    steps,tmp = Q.popleft()
    r, c = tmp[0], tmp[1]
    if (r, c) == (Y-1, X-1):
        print(steps)
    for x, y in moves:
        new_r, new_c = r+x, c+y
        if  0<=new_r<Y and 0<=new_c<X and (new_r, new_c) not in visited:
            Q.append((steps+1,(new_r,new_c)))
            print(Q)
            visited.add((new_r,new_c))
            print(visited)