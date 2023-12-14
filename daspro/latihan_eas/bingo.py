n,m = map(int,input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    ada = 0
    for j in range(m):
        if matrix[i][j] == 0:
            ada = 1
    if(ada == 1):
        print("BINGO!")
    else:  
        baris = matrix[i]
        kecil = min(baris)
        for x in range(0,n):
            if(baris[x] == kecil):
                baris[x] = 0
        no = 1
        for s in baris:
            print(s,end="")
            if(no != m):
                print(" ",end="")
            no+=1
        print()
        # Kalau gaada pilih elemen terkecil dari ganti itu dengan  0
        # cetak semua elemen
