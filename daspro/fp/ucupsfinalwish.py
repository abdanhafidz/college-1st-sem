n = int(input())
A = list(map(int, input().split()))

list_A = [A]

for i in range(n - 1):
    A_tmp = [A[j + 1] - A[j] for j in range(len(A) - 1)]
    list_A.append(A_tmp)
    A = A_tmp

hasil = sum(k[-1] for k in list_A)
print(hasil)