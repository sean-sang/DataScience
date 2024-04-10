import csv
import math

# Write Python functions to calculate and display the max, min, range, mean, mode, variance, and standard deviation for "MEDV". 
# function, takes in filename ('BostonHousing.csv') and column_name ('medv')
def calculate(filename, column_name):

    # Declaring variables
    min_val = 0
    max_val = 0
    sum_val = 0
    sum_squares = 0
    count = 0
    mode_val = mode_count = 0
    mode_dict = {} # initializes a dictionary to count occurences for mode
   

    # Opens provided filename in read only mode and passes it through csv.reader
    with open(filename, 'r') as file:
        column = csv.reader(file)
        header = next(column) #skips header
        column_index = header.index(column_name) #skips to 'medv' or column_name

        # for loop to read through the column
        for row in column: 
            value = float(row[column_index]) # turns values into floats for calculations
            # used to find min/max val while sorting through the column
            if min_val == 0 or value < min_val: # if the value is 0 or less than previous min_val then update with smaller value
                min_val = value
            if max_val == 0 or value > max_val: # if the value is 0 or larger than previous max_val then update with larger value
                max_val = value
            
            sum_val += value # Adds up each  value in the row within the column to find the total
            sum_squares += value**2 # Adds up each squared value in the row within the column to find the sum of squares
            count += + 1 # Counter to find the total number of elements in the column

            # Finding the mode for the column, as the for loop goes through each row
            mode_dict[value] = mode_dict.get(value, 0) # Adds/checks if the value inside the column is a key
            mode_dict[value] += 1 # Increments the value by 1 of relative key

            # Verifies if the value exists as a key in the dict or if the value is 0
            # If so, it will update the value in the dict as it loops
            if mode_count == 0 or mode_dict[value] > mode_count: 
                mode_val = value
                mode_count = mode_dict[value]

    # Using the values found during the for loop, we can find the range, mean, ariance, and SD.
    range_val = max_val - min_val
    mean_val = sum_val / count
    variance_val = (sum_squares - count * (mean_val**2)) / (count - 1)  # Sample variance formula instead of pop. variance per Professor Damavandi.
    standardDev = math.sqrt(variance_val) # Standard Deviation is the sqrt of variance

    # Returns all values needed for the project
    return max_val, min_val, range_val, mean_val, mode_val, variance_val, standardDev, sum_val


# Sorts all values within array 
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    # Choose the center (here, we simply use the middle element)
    center = arr[len(arr) // 2]

    # Creates 3 partitioned lists to hold values when sorting
    left, middle, right = [], [], []
    for value in arr:
        if value < center: # if value is less than center, append to left partition
            left.append(value)
        elif value == center: # if equivalent, keep as center
            middle.append(value)
        else: # else append to right partition
            right.append(value)

    # Recursive call to continue sorting through the column
    return quickSort(left) + middle + quickSort(right)

# Write Python functions to calculate and return 40 and 80 percentiles for "MEDV" using all three methods covered in the class.
def percentile(filename, column_name, percentile):
    # Opens the column and reads through the values as a dictionary
    with open(filename, 'r') as file:
        data = csv.DictReader(file)
        # Sorts the column using the quickSort function
        column_data = quickSort([float(row[column_name]) for row in data])

    # Method 1. The smallest value that is greater than k percent of the values:
    ## while-loop to check if current element is equal to the smallest value, if so it will iterate up once in the index
    element_1 = (percentile * len(column_data) + 99) // 100
    while column_data[element_1] == column_data[element_1 - 1]:
        element_1 += 1
    percentile_1 = column_data[element_1]

    # Method 2. The smallest value that is greater than or equal to k percent of values:
    element_2 = int((percentile / 100) * len(column_data)) 
    # no check for identical values, leaves as the returned value which can be equivalent
    percentile_2 = column_data[element_2]

    # Method 3. An interpolated value between the two closest ranks:
    element_3 = (percentile * len(column_data)) // 100
    fraction = (percentile * len(column_data)) % 100
    # if value is a not an integer, it will provide the interpolated value between
    # two different element values, upper and lower
    if fraction == 0:
        percentile_3 = column_data[element_3]
    else:
        lower = column_data[element_3]
        upper = column_data[element_3 + 1] # element incremented by 1
        percentile_3 = lower + (upper - lower) * (fraction / 100) # interpolated formula variation

    return percentile_1, percentile_2, percentile_3

# Return values from calculate function, providing required values for project 2
max_val, min_val, range_val, mean_val, mode_val, variance_val, standardDev, sum_val = calculate('BostonHousing.csv', 'medv')

# Call the function to find the 40th and 80th percentiles for 'medv'
p40_1, p40_2, p40_3 = percentile('BostonHousing.csv', 'medv', 40) # 40th percentile
p80_1, p80_2, p80_3 = percentile('BostonHousing.csv', 'medv', 80) # 80th percentile


# Write Python functions to calculate and display the max, min, range, mean, mode, variance, and standard deviation for "MEDV". 
# Print the results
print(f"==== MEDV Results ====")

print(f"Max: {max_val:.2f}")
print(f"Min: {min_val:.2f}")
print(f"Range: {range_val:.2f}")
print(f"Mean: {mean_val:.2f}")
print(f"Mode: {mode_val:.2f}")
print(f"Variance: {variance_val:.2f}")
print(f"Standard Deviation: {standardDev:.2f}")
print(f"Total: {sum_val:.2f}")

print("")

print("===== Percentiles =====")
print(f"Method 1 - 40th percentile {p40_1:.2f}") # 19.80
print(f"Method 1 - 80th percentile {p80_1:.2f}") # 28.40

print(f"Method 2 - 40th percentile {p40_2:.2f}") # 19.70
print(f"Method 2 - 80th percentile {p80_2:.2f}") # 28.20

# Method 3's interpolated values are in-between Method 1's & Method 2's results
print(f"Method 3 - 40th percentile {p40_3:.2f}") # 19.74
print(f"Method 3 - 80th percentile: {p80_3:.2f}") # 28.36


