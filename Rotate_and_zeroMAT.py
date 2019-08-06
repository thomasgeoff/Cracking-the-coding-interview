#7 Rotate matrix
from __future__ import print_function

data = [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 0, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
    ]   

def displayMatrix(mat,r,c): 
      
    for i in range(0,r): 
          
        for j in range(0,c): 
              
            print ("{0:0>2}".format(mat[i][j]), end = ' ') 
        print ("") 
    print("\n") 

def rotate(matrix):
    if matrix is None or len(matrix)<1:
        return
    else:
        if len(matrix)==1:
            return matrix
        else:
            #size of matrix
            m = len(matrix[0])
            #solution matrix
            soln = [row[:] for row in matrix]
#            print("1")
#            displayMatrix(soln,N)
            soln1 = [row[:] for row in matrix]
#            print("2")
#            displayMatrix(soln1,N)        
            print("Original Matrix \n----------------")
            displayMatrix(data[0],m,m)
                    
            for x in range(0,m):
                for j in range(0,m):
                    soln[j][m-1-x] = matrix[x][j]
                    soln1[m-1-x][j] = matrix[j][x]
            print("Rotated 90 degrees clockwise \n----------------------------")
            displayMatrix(soln,m,m)
            print("Rotated 90 degrees anti-clockwise \n---------------------------------")
            displayMatrix(soln1,m,m)
# Print rotated matrix 
rotate(data[0])

def zero_matrix(mat,r,c):
    m = n = None
    print("Original Matrix \n----------------")
    displayMatrix(mat,r,c)
    for i in range(0,r):
        for j in range(0,c):
            if mat[i][j] == 0:
                m = i
                n = j
#                print(m,n)
                break
        if m is not None:
            break
    for k in range(0,r):
                   mat[k][n]=0
#                   print(k,n) 
    for l in range(0,c):
                    mat[m][l]=0
#                    print(m,l)
    print("Zero Matrix \n-------------")    
    displayMatrix(mat,r,c)

zero_matrix(data[1],5,5)  
