alp = "abcdefghijklmnopqrstuvwxyz"
chrr = input()
n = int(input())
ans = ""

for x in chrr:
    if x in alp:
        idx = alp.index(x)
        shift = (n + idx ) % 26
        ans += alp[shift]
    else:
        ans += x

print(ans)