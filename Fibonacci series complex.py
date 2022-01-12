def square(max):
    a,b=0,1


    while a < max:
        yield a
        a,b=b,a+b



for i in square(6):
    print(i)












