def square():
    a,b=0,1


    while a < 6:
        yield a
        a,b=b,a+b

r=square()


print(r.next())
print(r.next())
print(r.next())
print(r.next())
print(r.next())
print(r.next())


for i in square(6):
    print(i)












