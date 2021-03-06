n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
res = 0
start = end = n//2

for i in range(n):
    for j in range(start, end+1):
        res += grid[i][j]
    if i < n//2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1

print(res)
