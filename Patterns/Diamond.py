print("Hello")
#n = int(input("Enter No. of Rows:"))
n = 5

for row in range(n-1):
    for column in range(row,n):
        print(" ",end=" ")
    for column in range(row):
        print("*",end=" ")
    for column in range(row+1):
        print("*",end=" ")
    print()

for row in range(n):
    for column in range(row+1):
        print(" ",end=" ")
    for column in range(row,n-1):
        print("*",end=" ")
    for column in range(row,n):
        print("*",end=" ")
    print()
