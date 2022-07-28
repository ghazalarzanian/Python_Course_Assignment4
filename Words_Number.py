from itertools import count


def Number_of_words(a):
    count=int(1)
    for i in range(len(a)):
        if a[i] ==" ":
          count +=1
    print(count)
A = str(input("Enter a sentnce(with no extra space):"))
Number_of_words(A)