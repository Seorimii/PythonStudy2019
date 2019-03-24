def getPrime(x):
    if x%2==0:
        return

    for i in range(3,int(x/2),2):
        if x%i==0:
            break
    else:
        return x

listdata = [17, 19, 113, 1113, 1119]
ret = filter(getPrime,listdata)
print(list(ret))
