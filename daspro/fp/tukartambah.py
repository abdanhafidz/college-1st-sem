
# try:
#     m = int(input())
#     s = list()
#     for _ in range(m):
#         s.append(input())
#     n = int(input())
#     for _ in range(n):
#         k = input()
#         k = k.split(" ")
#         tmp1 = s.index(k[0])
#         tmp2 = s.index(k[1])
#         s[tmp2] = k[0]
#         s[tmp1] = k[1]

#     for x in s:
#         print(x)
# except:
#     print()

def tt(kolom,k): 
    for i in range(len(k)): # 0 1
        if k[i][0] in kolom and k[i][1] in kolom:
            index1 = kolom.index(k[i][0]) # 0
            index2 = kolom.index(k[i][1]) # 1
            kolom[index1], kolom[index2] = kolom[index2],kolom[index1]
    return kolom

N = int(input())
kolom = [input().strip() for _ in range(N)]

x = int(input())
k = [input().split() for _ in range(x)]

hasil = tt(kolom,k)

for a in hasil:
    print(a)


