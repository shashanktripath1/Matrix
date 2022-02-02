r,c=tuple(map(int,input("Enter the number of rows and columns : ").split()))
matrix=[[int(input("Input elements in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
#finding sum of all elements of matrix
sum,count=0,0
for i in range(r):
    for j in range(c):
        sum+=matrix[i][j]
        count+=1
print("Sum of all elements of matrix = ",sum)
print("Total number of elements in matrix = ",count)
