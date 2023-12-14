
m,n = [int(V) for V in input().split()]
baris = []
for i in range(m):
    baris.append([int(V) for V in input().split()])

visited = [ [0 for i in range(n)] for i in range(m) ]
def dfs(x,y):
    if(x<0 or y<0 or x>m-1 or y>n-1):
        return 0
    elif(visited[x][y] == 0 and baris[x][y] == 1):
        visited[x][y] = 1
        res = 1
        res += dfs(x+1,y)
        res += dfs(x,y+1)
        res += dfs(x-1,y)
        res += dfs(x,y-1)
        return res
    else: 
        return 0

count = 0
size = []
for i in range(m):
    for j in range(n):
        if(visited[i][j] == 0):
            if(baris[i][j] == 1):
                count+=1
                size.append(dfs(i,j))
print("Banyak Pulau:",count)
s = ""
i = 1
for x in size:
    if(i!=len(size)):
        s+=str(x)+" "
    else:
        s+=str(x)
    i+=1
print("Luas Pulau:",s)

    
    
