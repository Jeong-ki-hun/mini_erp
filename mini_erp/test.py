maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
from collections import deque
def bfs(start,maps,end):
    vistied = [[0 for _ in range(len(maps[0]))]for _ in range(len(maps))]
    q = deque([])
    q.extend(start)
    len_x = len(maps)
    len_y = len(maps[0])
    while q:
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        x,y,cnt = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]

            if nx < 0 or ny < 0 or nx >= len_x or ny >= len_y or vistied[nx][ny] == 1 or maps[nx][ny] == "X":
                continue
            elif maps[nx][ny] == end:
                return cnt+1
            else:
                q.append((nx,ny,cnt+1))
                vistied[nx][ny] = 1
    return -1

def solution(maps):
    st = []
    en = []
    for i in range(len(maps)):
        if st and en:
            break
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                st.append((i,j,0))
            elif maps[i][j] == "L":
                en.append((i,j,0))
            if st and en:
                break

    if bfs(st,maps,"L") == -1 or bfs(en,maps,'E') == -1:
        return -1
    else:
        return bfs(st,maps,"L") + bfs(en,maps,'E')
    
print(solution(maps))