print("Hello")
#n = int(input("Enter No. of Rows:"))
n = 5
for row in range(n):
    for clolumn in range(row,n):
        print("*",end=" ")
    print()
