n = input("Saisissez un nombre: ")
n = int(n)
q = n
res=""

while q!=0:
    r = int(q%2)
    q = int(q/2)
    r2 = str(r)
    res+=r2
    print(res)

while q!=0:
    r = int(q%2)
    q = int(q/2)
    if r<=9:
        res+=r2
        print(res)
    else:
        if r==10:
            res="A"
            print(res)
        if r==11:
            res="B"
            print(res)
        if r==12:
            res="C"
            print(res)
        if r==13:
            res="D"
            print(res)
        if r==14:
            res="E"
            print(res)
        if r==15:
            res="F"
            print(res)