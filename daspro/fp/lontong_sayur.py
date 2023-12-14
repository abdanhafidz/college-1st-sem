import math

def dist(m, n, xr, yr, wr, hr, xu, yu):
    distance = math.sqrt((xr - xu)**2 + (yr - yu)**2)
    if x >= xr - wr / 2 and x <= xr + wr / 2 and y >= yr - hr / 2 and y <= yr + hr / 2:
        print("KAMU SUDAH SAMPAI")
    else:
        print("{:.2f} METER LAGI".format(distance))
m, n = map(int,input().split())
xr, yr, wr, hr = map(int,input().split())
x, y = map(int,input().split())
dist(m, n, xr, yr, wr, hr, x, y)