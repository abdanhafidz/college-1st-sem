
fib=[0,1,1,2,3]
for i in range(5,32):
    fib.append(fib[i-1] + fib[i-2])

def swapItem(item,n,item1,item2):
    if((fib[n]%2) == 1):
        idx1 = item.index(item1)
        idx2 = item.index(item2)
        tmp = item[idx1]
        item[idx1] = item[idx2]
        item[idx2] = tmp
    return item
N = int(input())
barang = []
for x in range(N):
    addbarang = input()
    barang.append(addbarang)
M = int(input())
for y in range(M):
    swap = list(map(str,input().split()))
    barang = swapItem(barang,int(swap[0]),swap[1],swap[2])
for x in barang:
    print(x)

# print(fib[17])


