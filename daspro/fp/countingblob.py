def blobbing(A, n):
 
    res = 0 
    curr = 1
    for i in range (n - 1) :
        if (A[i + 1] < A[i]):
            curr += 1
        else :
            res += (((curr - 1) * curr) // 2);
            curr = 1
    if (curr > 1):
        res += (((curr - 1) * curr) // 2)
    return res
N = int(input())
A = [map(int,input.split())]
print(blobbing(A,N))