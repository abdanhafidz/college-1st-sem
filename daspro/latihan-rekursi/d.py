def f(N, M) :
    if N > 100 :
        return 0
    elif N == M :
        return 0
    elif N == 100 :
        return 1
    else :
        sum = 0
        for i in range(1, 7) : #MENGITERASI ANGKA DADU 1 SAMPAI 6
            if N + i != M :
                sum += f(N + i, M)
        return sum
    
N, M = map(int, input().split())

res = f(N, M)
print(f"Ada {res} cara nih!")