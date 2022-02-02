r,c=tuple(map(int,input("Enter the number of rows and columns : ").split()))
matrix=[[int(input("Input element in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
print("The matrix is : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
#taking a resultant matrix
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(c):
        result[i][j]=matrix[j][i]
#printing the resultant matrix
print("Resultant matrix is : ")
for i in range(r):
    for j in range(c):
        print(result[i][j],end=" ")
    print()
