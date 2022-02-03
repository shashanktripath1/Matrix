r,c=tuple(map(int,input("Enter number of rows and columns :  ").split()))
matrix=[[int(input("Input element in matrix[%d][%d] : "))for i in range(c)]for j in range(r)]
print("Matrix is : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=' ')
    print()
sumd1,sumd2=0,0
for i in range(r):
    for j in range(c):
        if i==j:
            sumd1+=matrix[i][j]
        if i+j==r-1:
            sumd2+=matrix[i][j]
if sumd1!=sumd2:
    f=1
else:
    for i in range(r):
        sumr,sumc=0,0
        for j in range(c):
            sumr+=matrix[i][j]
            sumc+=matrix[j][i]
        if sumr!=sumd1:
            f=1
        elif sumc!=sumd1:
            f=1
        else:
            f=0
        
if f==0:
    print("Matrix is Magic square")
    print("Sum of diagonal 1= ",sumd1)
    print("Sum of diagonal 2= ",sumd2)
    print("Sum of Row = ",sumr)
    print("Sum of column = ",sumc)

    
else:
    print("Matrix is not Magic Square")
    print("Sum of diagonal 1= ",sumd1)
    print("Sum of diagonal 2= ",sumd2)
    print("Sum of Row = ",sumr)
    print("Sum of column = ",sumc)

    
