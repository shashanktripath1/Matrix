r,c=tuple(map(int,input("Enter the number of rows and columns : ").split()))
matrix=[[int(input("Input element in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
print("Entered matrix is : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
print("Matrix in alternate manner : ")
#logic to print matrix in alternate manner
for i in range(r):
    k=r-1
    for j in range(c):
        if i%2==0:#if alter way then write i%2!=0
            print(matrix[i][j],end=" ")
        else:
            print(matrix[i][k],end=" ")
            k-=1
    print()
