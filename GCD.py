def GCD(a,b):
    Min=int()
    if (a< b):
        Min = a
    else :
        Min=b
    for i in range(2,Min+1):
        if  a % i==0 and b%i==0:
            result = i
    print(result)
A = int(input("Eneter A: "))
B = int(input("Eneter B: "))
GCD(A,B)