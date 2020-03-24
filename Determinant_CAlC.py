import numpy as np

#A = [[1,2]
#   , [3,4]]
#ans = 0

# A = [[1, 2, 3]
#     ,[4, 5, 6]
#     ,[7, 8, 0]]
#ans = 27

# A = [[4, 1, 2]
#     ,[3, 2, 1]
#     ,[9, 3, 1]]
# # ans =-16


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


def deter(A,value):
    
    N = len(A)
    for i in range(N):
        if N == 2:
           value += A[0][0]*A[1][1] - A[0][1]*A[1][0]
           break
        else:
            B = np.delete(A,i,1)
            B = np.delete(B,0,0)
            value += (-1)**i*A[0][i]*deter(B,0)     
    return(value)

x = deter(A,0)
print(x)

