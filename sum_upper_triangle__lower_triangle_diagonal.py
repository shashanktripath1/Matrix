r,c=tuple(map(int,input("Enter the number of Rows and Columns : ").split()))
matrix=[[int(input("input element in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
print("Entered matrix is : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
#to find the sum of lower triangular elements,upper triangular elements,diagonal elements
sum_lower_triangle,sum_upper_triangle,sum_diagonal=0,0,0
for i in range(r):
    for j in range(c):
        if i>j:
            sum_lower_triangle=sum_lower_triangle+matrix[i][j]
        elif i<j:
            sum_upper_triangle+=matrix[i][j]
        elif i==j:
            sum_diagonal+=matrix[i][j]
print("Sum of lower triangle elements : ",sum_lower_triangle)
print("Sum of upper triangle elements : ",sum_upper_triangle)
print("Sum of diagonal elements : ",sum_diagonal)



            
