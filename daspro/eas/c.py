
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
x,y = map(int,input().split())

count = 0
island = []
print("Route for Luffy Journey:")
for i in range(m):
    for j in range(n):
        if(visited[i][j] == 0):
            if(baris[i][j] == 1):
                count+=1
                # print("Dari",y," ",x,"Pulau di ",i," ",j)
                dist = abs(((y)-i)) + abs(((x)-j))
                area = dfs(i,j)
                island.append([count,dist,area])

island.sort(key = lambda ind1:ind1[1])
island.sort(key = lambda ind1:ind1[2])
for x in island:
    print("Island ",x[0]," (Distance: ",x[1],", Area: ",x[2],")")

    
    
