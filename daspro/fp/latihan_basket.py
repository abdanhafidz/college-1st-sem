T = int(input())



def solve(N,K):
    midRest = N - N//2
    if(K<=midRest):
        return 2*K - 1
    else:
        if(N%2 == 1):
            return 2*(N//2) - 2*(K - midRest) + 2
        else:
            for i in range(2,N+1):
                if(i%2 == 0):
            return 
# U(K-Midrest) = 2 + 4(K - Midrest - 1) jika Un 
# K = 2*K - 1 , jika K < MidRest 
# Banyak bilangan Genap = N//2
# 4 Urutan ke berapa?
# 2 4 6 8
# Un = 2n
# 2 -> U1
# 4 -> U2
#...
# 8 -> U1
# 6 -> U2
# Bilangan genap terbesar dalam list = U(Banyak Bilangan Genap) = Un//2 = 2*(n//2)
# U(Midrest - K) = 2*(N//2) - 2*(Midrest-K) + 2
# Un = a + b(n-1)
# Un = 2*(N//2) + -2(n-1)
# Un = 2*(N//2) - 2n + 2
# 2n = 2*(N//2) + 2 - Un

# K = 2*(N//2) - 2n + 2 + MidRest
# (if(N ganjil)) -> N - 1 - 2n + 2 -> N + 1 - 2n + MidRest =  K -> n = (N + 1 - K)//2
# (if(N Genap)) -> N - 2n + 2 -> N + 2 - 2n + MidRest = K -> n = (N + 2 - K)//2

#  (Untuk K > MidRest)

# 1 2 3 4 5
# 1 2 3 4 5 (1 layout keluar)
# 2 3 4 5 (2 lay up)
# 3 4 5 2 (3 layout keluar)
# 4 5 2 (4 layup)
# 5 2 4 (5 layout Keluar)
# 2 4 (2 Layup)
# 4 2 (4 Layout Keluar)
# 2 (2 Layup)
# (2 Layout Keluar)


# 1 2 3 4 5 6
# 1 2 3 4 5 6 (1 layout keluar)
# 2 3 4 5 6 (2 layup)
# 3 4 5 6 2 (3 istirahat)
# 4 5 6 2 (4 layup)
# 5 6 2 4 (5 keluar)
# 6 2 4 (6 layup)
# 2 4 6 (2 keluar )
# 4 6 (4 layup)
# 6 4 (6 keluar)
# 4 (4 layup)
# 4( 4 keluar)


# 1 2 3 4 5 6 7 8 9 10 
# 2 3 4 5 6 7 8 9 10 (1 istirahat)
# 3 4 5 6 7 8 9 10 2 (2 kebelakang)
# 4 5 6 7 8 9 10 2 (3 istirahat)
# 5 6 7 8 9 10 2 4 (4 ke belakang)
# 6 7 8 9 10 2 4 (5 istirahat)
# 7 8 9 10 2 4 6 (6 Ke belakang)
# 8 9 10 2 4 6 (7 istirahat)
# 9 10 2 4 6 8 (8 ke belakang)
# 10 2 4 6 8 (9 istirahat)
# 2 4 6 8 10 (10 ke belakang)
# 4 6 8 10 (2 istirahat)
# 6 8 10 4 (4 ke belakang)
# 8 10 4 (6 istirahat)
# 10 4 8 (8 ke belakang)
# 4 8 (10 istirahat)
# 8 4 (4 ke belakang)
# 4 (8 istirahat)
# 4 k
# 1 3 5 7 9
# 2 6 10 8 4

# N = 6 -> 2 6 4
for i in range(0,T):
    N,K = map(int,input().split())
    print(solve(N,K))