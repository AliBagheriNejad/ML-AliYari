from sympy import Matrix, det, sin, cos, symbols,solve

# Defining symbols for theta and lambda
theta = symbols('theta')
lam = symbols('lambda')

# Rotaiont matrix in 2D
rotation_matrix = Matrix(
    [
    [cos(theta),-sin(theta)],
    [sin(theta),cos(theta)],
    ],
    )

# Eigen values
values = rotation_matrix.eigenvals()
eigenvlaues = list(values.keys())
values = [value.simplify() for value in values]

# Eigen vectors
vectors = rotation_matrix.eigenvects()
vectors = [vec[2] for i,vec in enumerate(vectors)]

# Showing the eigenvalues and eigenvectors
print(f'EigenValues are:\n\t\t{values[0]}\n\t\t{values[1]}',end='\n'*3)
print(f'EigenVectors are:\n\t\t{vectors[0]}\n\t\t{vectors[1]}',end='\n'*3)
