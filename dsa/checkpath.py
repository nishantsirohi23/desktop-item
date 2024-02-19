grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

if not grid:
    print(0)

rows , cols = len(grid),len(grid[0])
visited = set()
island = 0

def bfs(r,c):
    q = deque()
    visited.add((r,c))
    q.append((r,c))

    while q:
        row,col = q.popleft()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for dr,dc in directions:
            r,c = row+dr,col+dc
            if ()

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "1":
            bfs(r,c)
            island+=1

print(island)