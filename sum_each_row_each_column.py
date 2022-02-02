r,c=tuple(map(int,input("Enter the number of rows and columns : ").split()))
matrix=[[int(input("Input element in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
print("The matrix is : ")
row,column=0,0
ro=[]
co=[]
for i in range(r):
    for j in range(c):
        row=row+matrix[i][j]
        column=column+matrix[j][i]
    ro.append(row)
    co.append(column)
    row=0
    column=0

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print(ro[i],end=" ")
    print()
for i in range(3):
    print(co[i],end=" ")
