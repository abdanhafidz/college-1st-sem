L,M,K = map(int,input().split())
MOD = 10**9 + 7
res = 0
res = (sum( ((M + i for i in range(1,K)) % MOD)**L) ) %MOD
res+= ((K%MOD)**L)%MOD
print(res)