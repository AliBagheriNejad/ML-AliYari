import timeit
import numpy as np
import matplotlib.pylab as plt

setup = '''import numpy as np

# Creating matrices
m, n = 20, 10
A = np.random.rand(m, n)
k = np.random.rand(n)
p1 = np.zeros(m)
'''
# Creating matrices
m, n = 20, 10
A = np.random.rand(m, n)
k = np.random.rand(n)
p1 = np.zeros(m)

method1 = '''# For loop
for i in range(n):
    
    p1 += A[:,i]*k[i]
'''
# For loop
for i in range(n):
    
    p1 += A[:,i]*k[i]
    
method2 = '''
# Vector implementation
p2 = np.dot(A,k)
'''
# Vector implementation
p2 = np.dot(A,k)


# Loop to calculate time for each method
Loop = []
Vec = []
for i in range(1000):
    
    # Duration of loop method
    with_loop = timeit.timeit(
        setup=setup,
        stmt=method1,
        number=i
        )
    Loop.append(with_loop)
    # Duration of vector implementation method
    with_vec = timeit.timeit(
        setup=setup,
        stmt=method2,
        number=i
        )
    Vec.append(with_vec)

# Plotting the outcome
plt.figure(figsize=(10,7))
plt.plot(Loop)
plt.plot(Vec)
plt.title('Comparison of the dutation of each method')
plt.xlabel('Number of iterations of the method')
plt.ylabel('Time(second)')
plt.legend(['For loop', 'Vector implementation'])
plt.grid(which='major')

# Check if the outcomes are the same
are_they = np.allclose(p1,p2)

if are_they:
    print(f'outcome of loop method: {p1}',end='\n\n')
    print(f'outcome of vectro implementation method: {p2}',end='\n\n')
    print('The outcome of both methods is the same vector')
else:
    print('The outcome of methods are different')