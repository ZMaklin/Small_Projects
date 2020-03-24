### Square Matrix Determinant Calculator ###

## Notes ##
 # - Keep "Value" as Zero always in the fucntion
 # - "A" can be a square matrix of size up to 5X5
 # - Greater size matrices result in extremely long run times or huge determinants

import numpy as np
def deter(A,value):
     
    N = len(A)
    for i in range(N):
        if N == 2: # if the matirx has dimensions of 2X2 solve the matrix and add its result to "value"
           value += A[0][0]*A[1][1] - A[0][1]*A[1][0] #solve the matrix and add its result to "value"
           break
        else:
            B = np.delete(A,i,1) # Creates a new matrix by removing the 'i'th column
            B = np.delete(B,0,0) # removes the top row from the new matrix
            value += (-1)**i*A[0][i]*deter(B,0) # This adds the multiplier to the matirx and the sign is dictated by the -1 to the 'i'
    return(value)



### Example Test Cases ###


#### 2X2
#A = [[1,2]
#   , [3,4]]
#ans = 0


#### 3X3
# A = [[4, 1, 2]
#     ,[3, 2, 1]
#     ,[9, 3, 1]]
# # ans =-16

#### 4x4
# A = [[ 1,  3,  5,  9]
#     ,[ 1,  3,  1,  7]
#     ,[ 4,  3,  9,  7]
#     ,[ 5,  2,  0, 15]]

#### 5X5
A = [[ 1,  2,  3,  3, 5]
    ,[ 2,  4,  3,  3, 5]
    ,[ 9, 14, 11, 12, 5]
    ,[13, 14, 15,  0, 5]
    ,[ 2,  2,  2,  3, 4]]
#ans = 1704


x = deter(A,0)
print(x)

