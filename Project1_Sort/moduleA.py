# Part 1
# Merge Sort, Write a python function to merge sort a list of numbers. Test your function on a small random integer list of 10 elements.
def mergeSort(list):
    if len(list) > 1: #if length of provided list is greater than 1, it will begin sorting. No reason to sort a list with 1 element.
        mid = len(list) // 2 #splitting the list in half
        lhs = list[:mid] #lhs operation
        rhs = list[mid:] #rhs operation
        mergeSort(lhs) #recursive lhs call
        mergeSort(rhs) #recurise rhs call
        i = 0 #lhs iterator
        j = 0 #rhs iterator
        k = 0 #main iterator
        # main algorithm to sort through list
        while i < len(lhs) and j < len(rhs):
            if lhs[i] <= rhs[j]: # if lhs is less than rhs, it adjusts lhs operator, i, by an increment of 1 on the list
              list[k] = lhs[i]
              i += 1
            else:
                list[k] = rhs[j] # else it will adjust rhs, j, iterator by an increment of 1
                j += 1
            k += 1
        # if there are leftover elements in the leftover halves, it will continue cycling
        while i < len(lhs): # cycles lhs
            list[k] = lhs[i]
            i += 1
            k += 1
        while j < len(rhs): #cycles rhs
            list[k]=rhs[j]
            j += 1
            k += 1
    # returns the sorted list 
    return list

# Turns all values in the dictionary to CM by multiplying the values by 2.54
# round allows it to keep the values up to 2 decimal points
def intoCM(dict):
    return {key: round(value * 2.54, 2) for key, value in dict.items()}

# Allows you to enter the dict. and outputs the lowest value
# Variable dict is the dictionary to check values and find the lowest value
def lowestFall(dict):
    lowestRainfall = 0
    lowestKey = 0
    # Cycles through the entire dict. checking the values
    for key, value in dict.items():
        # If the value in the dict is lesser than the value than it will shift the key position, ultimately providing the smallest value
        # Since we have lowestRainfall set as 0 at the start, it will run the loop at least once. Afterward it will continue 
        # cycling through until we can find the lowest rainfall value
        if  lowestRainfall == 0 or value < lowestRainfall:
            lowestRainfall = value
            lowestKey = key

    return lowestKey


# The same as lowestFall, just changes the greater than to less than
# Variable dict is the dictionary to check values and find the largest value
def largestFall(dict):
    largestRainfall = 0
    largestKey = 0
    #Cycles through the entire dict. checking the values
    for key, value in dict.items():
        # If the value in the dict is larger than the value than it will shift the key position, ultimately providing the largest value
        # Since we have largestRainfall set as 0 at the start, it will run the loop at least once. Afterward it will continue 
        # cycling through until we can find the lowest rainfall value
        if largestRainfall == 0 or value > largestRainfall:
            largestRainfall = value
            largestKey = key
    return largestKey

# Variable is the dict. to check all values and use a counter to find length to divide against and find mean
def meanRainfall(dict):
    counter = 0
    sum = 0
    for value in dict.values():
        sum += value
        counter += 1
    return sum / counter
# variable 'dict' is the dict you want to check if there are values/keys that are larger than the variable 'value'
# using meanRainfall for value
def greaterThan(dict):
    counter = 0
    for key, value in dict.items():
        # if the value within the dict is larger than the input value, then it will increment the counter by 1 
        if value > meanRainfall(dict): # plugging in meanRainfall FN as the value to check against
            counter += 1
    # outputs the counter value (all months greater than the provided value)    
    return counter

# sorting the values dates based on dict. values
def bubble_sort(dict):
  # turns month to list to be able to sort through
    month_values = list(dict.items())

# standard bubble sort, goes through month_values to find largest/smallest values
    for i in range(len(month_values) - 1):
        for j in range(len(month_values) - 1 - i):
            if month_values[j][1] < month_values[j + 1][1]:
                month_values[j], month_values[j + 1] = month_values[j + 1], month_values[j]
  
# returns the sorted dictionary values    
    return month_values
