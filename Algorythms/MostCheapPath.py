from collections import deque

grid = [[1,3,1],[1,5,1],[4,2,1]]

#Count most cheap path, quite slow
Y, X = len(grid), len(grid[0])
moves = [(0,1),(1,0)]
Q = deque()
Q.append((1,(0,0)))
buffer = [e.copy() for e in grid]

while Q:
    steps,tmp = Q.popleft()
    r, c = tmp[0], tmp[1]
    for x, y in moves:
        new_r, new_c = r+x, c+y
        if  0<=new_r<Y and 0<=new_c<X:
            if grid[new_r][new_c] == buffer[new_r][new_c]:
                buffer[new_r][new_c] += buffer[r][c]
            else:
                new_sum = grid[new_r][new_c] + buffer[r][c]
                old_sum = buffer[new_r][new_c]
                if new_sum < old_sum:
                    buffer[new_r][new_c] = new_sum
            Q.append((steps+1,(new_r,new_c)))

print(buffer[-1][-1])

#same but fast
Y, X = len(grid), len(grid[0])

for y in range(1, Y):
    grid[y][0] += grid[y-1][0]
for x in range(1, X):
    grid[0][x] += grid[0][x-1]
for y in range(1, Y):
    for x in range(1, X):
        grid[y][x] += min(grid[y-1][x], grid[y][x-1])

print(grid[-1][-1])