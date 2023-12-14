M = int(input())
menu = []
for y in range(M):
    menu.append(list(map(str,input().split())))
k,m = map(str,input().split())
if(m == "S"):
    menu.sort(key = lambda ind1:ind1[2])
    menu.sort(key = lambda ind2:int(ind2[1]))
    menu.sort(key = lambda ind3:int(ind3[0]))
    menu = menu[::-1]
    for x in range(0,int(k)):
        print(" ".join(menu[x]))
elif(m == "P"):
    menu.sort(key = lambda ind2:ind2[0])
    menu.sort(key = lambda ind3:int(ind3[2]))
    menu.sort(key = lambda ind1:int(ind1[1]))
    menu = menu[::-1]
    for x in range(0,int(k)):
        print(" ".join(menu[x]))
elif(m == "Q"):
    menu.sort(key = lambda ind3:ind3[0])
    menu.sort(key = lambda ind2:int(ind2[1]))
    menu.sort(key = lambda ind1:int(ind1[2]))
    menu = menu[::-1]
    for x in range(0,int(k)):
        print(" ".join(menu[x]))
    