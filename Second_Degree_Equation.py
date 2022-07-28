from math import sqrt
from math import pow

def Second_Degree_Equation(a,b,c):
    if (pow(b,2)-(4*a*c)) < 0:
        print("wrong")
    else:
        delta=sqrt((pow(b,2)-(4*a*c)))
        x1 =((-b)+delta) / (2*a)
        x2 =((-b)-delta) / (2*a)
        print(x1,",",x2)
print(" ax^2 + bx + c")
A = float(input("Enter a: "))
B = float(input("Enter b: "))
C= float(input("Enter c: "))
Second_Degree_Equation(A,B,C)
#ax^2 + bx + c