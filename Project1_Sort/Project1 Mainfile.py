import moduleA
# A main code to call all above functions and return required values in centimeters.
# Write a python function to merge sort a list of numbers. Test your function on a small random integer list of 10 elements.

# sample data list of 10 int
randList = [3456, 12, 123, 261, 38, 141, 2, 5123, 5, 9]
# mergeSort(randList) # Sorted data: [2, 12, 38, 123, 141, 261, 3456, 5123]
print("The list of data beforehand was:\n{}".format(randList))
print("Now that it is sorted, it is:\n",(moduleA.mergeSort(randList)))
print("")



# commands to retrieve all corresponding data
# Part 2 Modules and Functions
# A function that returns the month with highest/largest rainfall.
# A function that returns the month with lowest/smallest rainfall.
# A function that returns the mean value of rainfall .
# A function that returns the number of months with rainfall greater than the mean value.
# A function to sort months with highest to smallest amount of rainfall using bubble sort.
#creates the yearly logged rainfall as a dictionary

weather = {"01" : 133.5, "02": 64.3, "03": 104.4, "04": 86.3, "05": 48.5, "06": 35.4, "07": 55.3, "08": 84.9, "09": 104.5, "10": 104.4, "11": 122.6, "12": 119.5}
weather = moduleA.intoCM(weather) # turns the values into cm by multiplying by 2.54

print("The month with the lowest rainfall is {:s}" .format(( moduleA.lowestFall((weather))))) 
print("The month with the most rainfall is {:s}" .format(( moduleA.largestFall((weather)))))
print("The average rainfall over the year is {:.2f} cm " .format(moduleA.meanRainfall((weather))))
print("The amount of months that have greater than average rainfall are:", moduleA.greaterThan(weather))
print("These are the months sorted by rainfall:", moduleA.bubble_sort(weather))
