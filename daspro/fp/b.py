n = int(input())
arr = list(map(int, input().split()))
num = [0] * 1000001
ans = 0

for i in range(n-1, -1, -1):
    if not num[arr[i]-1]:
        num[arr[i]] += 1
    else:
        num[arr[i]] += 1
        num[arr[i]-1] -= 1

for i in range(1, 1000001):
    ans += num[i]

print(ans)