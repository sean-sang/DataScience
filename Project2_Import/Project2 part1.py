import numpy as np

# function to pull coefficients from input file (input.txt)
def linear_eq(input):
    with open(input, 'r') as file: # opens input file in read only mode
        lines = file.readlines() # read through individual lines and save them in lines variable
        coefficients = [list(map(int, line.split())) for line in lines] # stores each int as a list called coefficients
        A = [coeff[:-1] for coeff in coefficients] # every int up until the last int is saved as matrix A
        b = [coeff[-1] for coeff in coefficients] # for the last int in the row, its saved as vector b
        return np.array(A), np.array(b) # returns both values for linal.g


# Run the fn to pull coefficients from input.txt to be used for np.linalg
A_matrix, b_vector = linear_eq("input.txt")

# Calculate the inverse of A_matrix
# A_inverse = np.linalg.inv(A_matrix)
# # Calculate the solution by multiplying A_inverse with b_vector
# solution = np.dot(A_inverse, b_vector)

# using linalg.solve to speed up process
# numpy solve for linear matrix equation pulled from linear_eq function
solution = np.linalg.solve(A_matrix, b_vector)

# Toggle to print matrix and vector for testing if needed
# print(A_matrix)
# print(b_vector)

# for loop to print the variables

variables = ['x', 'y', 'z', 'w'] # defining variable names per project instruction example
# for loop to print through the variables followed the solutions from
# the solution variable provided by np.linalg.solve
for i, var in enumerate(variables): 
    print(f"{var} = {solution[i]:.2f}")

