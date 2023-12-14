harga = int(input())
p25 = 0
p100 = 0
p50 = 0
p20 = 0
p10 = 0
p5 = 0

p25+=harga/250
harga -= p25*250
p100+=harga/100
harga -= p100*100
p50+=harga/50
harga -= p50*50
p10+=harga/10
harga -= p10*10
p5 += harga/5
harga -= p5*5

if(harga == 0):
    print(p25," 250 ribuan","\n")
    print(p100," 100 ribuan","\n")
    print(p50," 50 ribuan","\n")
    print(p10," 10 ribuan","\n")
    print(p5," 5 ribuan","\n")
else:
    print("Harganya Jelek :(")


