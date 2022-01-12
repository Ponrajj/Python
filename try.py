n = int(input("enter the no. : "))
sum = 0
for i in range(1,n+1):
    if(i<n):
        print(i,"+", end=" ")
    else:
        print(i,end=" ")
    sum = sum + i
print("=",sum)