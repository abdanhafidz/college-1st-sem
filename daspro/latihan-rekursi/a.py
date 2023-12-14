try:
    def find(dungeon):
        n = len(dungeon)
        m = len(dungeon[0])
        
        for i in range(n):
            for j in range(m):
                if dungeon[i][j] == 'S':
                    s = (i, j)
                if dungeon[i][j] == 'E':
                    e = (i, j)

        q = [(s, [])]
        visited = set()

        while q:
            (x, y), p = q.pop(0)

            if (x, y) == e:
                return p

            if (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and dungeon[nx][ny] != '#' :
                        q.append(((nx, ny), p + [(nx, ny)]))
        
        return None

    def display_dungeon(dungeon, path):
        n = len(dungeon)
        m = len(dungeon[0])
        dc = [list(row) for row in dungeon]

        for x, y in path:
            if dc[x][y] != 'E':
                dc[x][y] = 'x'
        
        for i in range(n):
            for j in range(m):
                print(dc[i][j], end='')
            print()

    n, m = map(int, input().split())
    d = [input() for _ in range(n)]
    p = find(d)

    if p:
        display_dungeon(d, p)
    else:
        print("tempat mulai atau tempat tujuan tak tergambar")
except:
    print("tempat mulai atau tempat tujuan tak tergambar")