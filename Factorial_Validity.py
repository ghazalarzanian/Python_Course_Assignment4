def Factorial_Validity(a):
    count =int(1)
    i=int(2)
    while count < a:
        count = count *i
        i +=1
    if count == a or a ==1:
        print("right")
    else :
        print("Wrong")

def factoria(b):#with another algorithm
    result =int()
    i =int(2)
    while i <=b:
        result=b /i
        b = result
        i+=1
    if b ==1 :
        print("right")
    else:
        print("Wrong")
A = int(input("Enter a number:"))
Factorial_Validity(A)
factoria(A)