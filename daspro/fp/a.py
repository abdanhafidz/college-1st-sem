import math

X,Y = map(int,input().split())
gcd = str(math.gcd(X,Y))

if(len(gcd) % 2 == 0):
    print("Yey brankas berhasil dibuka :D")
else:
    print("Yah gagal :(")