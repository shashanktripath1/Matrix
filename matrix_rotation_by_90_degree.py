r,c=tuple(map(int,input("Enter the number of rows and columns : ").split()))
matrix=[[int(input("Input element in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
print("The matrix is : ")
#printing the matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
#finding transpose of a matrix
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(c):
        result[i][j]=matrix[j][i]
print("Transpose of a matrix is : ")
for i in range(r):
    for j in range(c):
        print(result[i][j],end=" ")
    print()
mirror=[[0,0,0],[0,0,0],[0,0,0]]
#rotating matrix by 90 degree
print("Matrix after rotation of 90 degree : ")
for i in range(r):
    n=c-1
    for j in range(c):
        mirror[i][j]=mirror[i][j]+result[i][n]
        n=n-1
for i in range(r):
    for j in range(c):
        print(mirror[i][j],end=" ")
    print()
