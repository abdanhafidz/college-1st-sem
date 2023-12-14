S = input()
r = S.split(" ")
sum = 0
for i in range(0,len(r)):
    sum += int(r[i])

avg = sum / len(r)
print("%.2f" % avg)