try:
    memo = [-1 for x in range(55)]
    memo[0] = ""
    memo[1] = "*"
    memo[2] = "**"
    def f(n):
        if(memo[n] != -1):
            return memo[n]
        else:
                memo[n] = f(n-2)+"\n"
                memo[n] += "*"*n+"\n"
                memo[n] += f(n-2)
        return memo[n]
    n = int(input())
    print(f(n))
except:
    exit()