# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
# Can you do this in place? 
def rotateMatrix(matrix): 
    n = len(matrix)
    m = int(n/2)
    y = n -1 
    for i in range(0, m):
        for j in range(i, n -1- i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[y-j][i]
            matrix[y-j][i] = matrix[y-i][y-j] 
            matrix[y-i][y-j] = matrix[j][y-i]
            matrix[j][y-i] = temp
    return matrix

def displayMatrix( mat, N):       
    for i in range(0, N): 
        for j in range(0, N): 
            print (mat[i][j], end = ' ') 
        print ("") 


mat = [ [1, 2, 3, 4 ], 
    [5, 6, 7, 8 ], 
    [9, 10, 11, 12 ], 
    [13, 14, 15, 16 ] ] 

rotateMatrix(mat)
displayMatrix(mat, 4 )

