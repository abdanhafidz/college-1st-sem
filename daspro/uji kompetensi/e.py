A = input()
B = input()
K = int(input())
B = B.split(" ")
P = A.split(" ")
N = P[0]
M = P[1]
count = []
for i in range(1,1001):
    count.append(0)
elemen = {}
for i in range(1,int(N)):
    count[int(B[i])] += 1
print(count[K])