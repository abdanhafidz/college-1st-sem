N, M = map(int, input().split())
petak = []
for _ in range(M):
    petak.append([int(V) for V in input().split()])
check = [[0] * N for _ in range(M)]
def f(x,y):
    if x >= M or y >= N or x < 0 or y < 0:
        return 0
    elif(x == M - 1 and y == N - 1):
        check[x][y] = 1
        return 1 
    else:
        if(petak[x][y] == 1):
            check[x][y] = 1
            if(f(x,y+1)): return 1
            if(f(x+1,y)): return 1
        check[x][y] = 0
    return 0
f(0,0)
if(check[0][0] == 0 or check[M - 1][N - 1] == 0):
    print("Hari ini Bunda nggak masak")
else:
    for i in range(0,M):
        for j in range(0,N):
            if(j != N - 1):
                print(f"{check[i][j]} ",end="")
            else:
                print(f"{check[i][j]}",end="")
        print()
    
    