import numpy as np

# Creating a random upper triangular matrix
d = 4
matrix = np.random.rand(d,d)
upper_tri = np.triu(matrix)
print(f'the matrix craeted is:\n{upper_tri}',end='\n\n')

# Randomly set one element of the main diameter to zero
random_number = np.random.randint(0,d,(1,))
if random_number%2 == 0:
    
    upper_tri[random_number,random_number] = 0
    print(f'The {random_number}th element is set to zero',end='\n\n')
    print(f'The new matrix is:\n{upper_tri}')
else:
    
    print('No element on the main diagonal is set to zero',end='\n\n')

# Product of elements on main diameter
product = 1
for i in range(d):
    
    product *= upper_tri[i,i]

# determinant of the matrix
det = np.linalg.det(upper_tri)

# Comparison
error = np.abs(product-det) 
if error <= 10**-7:
    
    print('The determinant of the martix and the product of the main diameter are the same ')
    print(f'Determinant = {det}')
    print(f'Product = {product}')
    print(f'The difference is {error:.5f}')
else :
    
    print('The determinant of the martix and the product of the main diameter are "not" the same')
    print(f'Determinant = {det}')
    print(f'Product = {product}')
    print(f'The difference is {error:.5f}')