memo = [-1 for i in range(10**5)]
memo[0] = 1
memo[1] = 1
memo[2] = 1
memo[3] = 2
memo[4] = 3
memo[5] = 5
def f(n):
    if(memo[n] != -1):
        return memo[n]
    else:
        if(n>0):
            memo[n] = f(n-1)+f(n-3)+f(n-5)
        else:
            memo[n] = 0
        return memo[n]

T = int(input())
N = map(int,input().split())
for n in N:
    print(f(n))
