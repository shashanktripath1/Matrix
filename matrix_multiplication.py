def input_matrix(r,c):
    matrix=[[int(input("Input elements in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
    return matrix
def print_matrix(matrix):
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()
#working on first matrix        
r,c=tuple(map(int,input("Enter the number of rows and columns in matrix 1 : ").split()))
print("Input elements in matrix 1 : ")
a=input_matrix(r,c)
#working on second matrix
r,c=tuple(map(int,input("Enter the number of rows and columns in matrix 2 : ").split()))
print("Input elements in matrix 2 : ")
b=input_matrix(r,c)
#printing first matrix
print("Matrix 1 is : ")
print_matrix(a)
#printing the second matrix
print("Matrix 2 is : ")
print_matrix(b)
#taking resultant matrix
result=[[0,0,0],[0,0,0],[0,0,0]]
#doing multiplication of two matrices
for i in range(r):
    for j in range(c):
        for k in range(r):
            result[i][j]=result[i][j]+a[i][k]*b[k][j]
#printing resultant matrix
print("Resultant matrix is : ")
for i in range(r):
    for j in range(c):
        print(result[i][j],end=" ")
    print()
