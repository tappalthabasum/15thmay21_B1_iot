n = int(eval(input('entr the jorder of matrix:')))
matrix = [[0 for i in range(n)] for y in range(n)]

i,j = 0,0
for x in range(1,(n**2)+1):
    if i == -1 and j == n:
        i = 0
        j = n-2
    elif i == -1:
        i = n-1
    elif j == n:
        j = 0
    if matrix[i][j] != 0:
        i+=1
        j-=2
    if x == 1:
        i = int(n/2)
        j = n-1
        matrix[i][j] = x
    else:
        matrix[i][j] = x
    i = i-1
    j = j+1
print('sum of each row or column: {}'.format(int(n*(n*n+1)/2)))
for x in matrix:
    print(x)
        
