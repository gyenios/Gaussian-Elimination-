import numpy as np

'''
Remember Ax = B

A is the matrix containing the coefficients of the variables

x represents the variables whose values are to be found

B is the column matrix containing the constants at the RHS of our equations
'''

def gaussian_elimination(mat_A,mat_B):
    # Adding some contingencies to prevent future problems

    # 1. Making sure that A is a square matrix
    if mat_A.shape[0] != mat_A.shape[1]:
        print('ERROR, square matrix mot given!')
        return
    
    # 2. Making sure that the constant vector B is a single column
    if mat_B.shape[0] > 1 or mat_B.shape[0] != mat_A.shape[0]:
        print('ERROR: Constant vector incorrectly sized')
        return

    print('Matrix is acceptable')
    # Initialization of necessary variables
    n = len(mat_B)
    m = n - 1
    i = 0
    j = i - 1
    x = np.zeros(n)
    new_line = '\n'

    # Creating an augmented matrix through Numpy's concatenate feature
    mat_augment = np.concatenate((mat_A,mat_B),axis = 1, dtype = float)
    print(f'The initial augmented matrix is: {new_line}{mat_augment}')
    print('Solving for the upper-triangular matrix:')

    # Applying Gauss Elimination:
    while i < n:
        if mat_augment[i][i] == 0.0: # Fail-safe to eliminate divide by zero-error!
            print('Divide by zero error')
            return
        for j in range(i + 1,n)
        multiplier = mat_augment[j][i] / mat_augment[i][i]
        mat_augment[j] -= multiplier*mat_augment[i]
        print(mat_augment) # Not needed but nice to re-visualize the process
        i += 1

    #Backwards substitution
    x[m] = mat_augment[m][n]/mat_augment[n][m]

    for k in range(n-2, -1, -1):
        x[k] = mat_augment[k][n]

        for j in range(k + 1, n):
            x[k] = x[k] / mat_augment[k][k]

    # Displaying solution
    print(f'The following x-vector matrix solves the above augmented matrix:')
    for answer in range(n):
        print(f'x{answer} is {x[answer]}')

mat_A = np.array([[2,1,3],[15,2,0],[1,3,12]])
mat_B = np.array([[10],[5],[3]])

gaussian_elimination(mat_A,mat_B)
