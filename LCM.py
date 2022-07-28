def LCM(a,b):
    result =0
    i=int(1)
    j=int(1)
    x=int()
    y =int()
    while result==0:
        x=a*i
        y=b*j
        if x == y:
            result=x
        else:
            if x<y :
                i+=1
            else:
                 j+=1
    print(result)
A = int(input("Eneter A: "))
B = int(input("Eneter B: "))
LCM(A,B)