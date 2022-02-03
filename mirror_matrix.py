r,c=tuple(map(int,input("Enter the number of rows and columns : ").split()))
matrix=[[int(input("Input element in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
print("The matrix is : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
mirror=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    n=c-1
    for j in range(c):
        mirror[i][j]=mirror[i][j]+matrix[i][n]
        n=n-1
print("The Mirror matrix is : ")
for i in range(r):
    for j in range(c):
        print(mirror[i][j],end=" ")
    print()
