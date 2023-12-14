n,m = map(int,input().split())
X,Y = map(int,input().split())
A = [list(map(int, input().split())) for i in range(n)]

def f(x,y):
    if( (x == n and y == ) or x<0 or y<0):
        return 0
    else:
        return (max(f(x+1,y),f(x,y-1)) + A[x][y])
print(f(X,Y))