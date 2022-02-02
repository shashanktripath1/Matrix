r,c=tuple(map(int,input("Enter the number of rows and columns : ").split()))
matrix=[[int(input("input element in matrix[%d][%d] : "%(j,i)))for i in range(c)]for j in range(r)]
print("Matrix is : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=' ')
    print()
l=[]
s=[]
#appending the upper triangular elements in list l and lower traingular elements in list2
for i in range(r):
    for j in range(c):
        if i<j:
            l.append(matrix[i][j])
        elif i>j:
            s.append(matrix[i][j])
#taking 2 variables and initialising it with zero so that we can use it in our logic
k=0
x=0
#swapping logic
for i in range(r):
    for j in range(c):
        if i>j:
            matrix[i][j]=l[k]
            k+=1
        elif i<j:
            matrix[i][j]=s[x]
            x+=1
#printing matrix after swapping
print("Matrix after swapping upper and lower triangular elements : ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=' ')
    print()           
        
