def Mul_Table(n,m):
    C = int(1)
    B = int(1)
    for i in range(n):
        print('\n')
        for j in range(m):
            print(C *B," , ",end='')
            C +=1
        C =1
        B +=1
    pass
N= int(input("Enter N: "))
M =int(input("Enter M:"))
Mul_Table(N,M)