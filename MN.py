def A( a ,b):
    for j in range(1,a+1):
        print("\n")
        if (j %2) != 0:#satr fard
            for i in range(1,b+1):
                if (i %2) == 0:#soton zooj
                    print("*",end='')
                else :
                    print("#",end='')
        else:#satr zoj
            for k in range(1,b+1):
                if (k %2) == 0:#soton fard
                    print("#",end='')
                else :
                    print("*",end='')
N =int(input("Enter N(Row): "))
M =int(input("Enter M(Col): "))
A(N,M)