r,c=tuple(map(int,input("Enter the number of rows and columns : ").split()))
def input_matrix(r,c):
    matrix=[[int(input("Input elements in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
    return matrix
def print_matrix(matrix):
    print("Matrix is : ")
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()
    
a=input_matrix(r,c)
print_matrix(a)
