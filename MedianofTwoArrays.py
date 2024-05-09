#This program will look at arrays of a variable size and get the median number of the two arrays. 
#Example [1, 2, 4], [3, 5, 4] = [1, 2, 3, 4, 4, 5], Median is 3.5

import array as arr
import math

#Function to determine the median of any single array.
def arr_median(arr):
    length = len(arr)
    half_length = length // 2 #Keep this a fkn integer
    print("median length", half_length)
    #Checks if the array has even number of elements.
    if length % 2 == 0: 
        median = (arr[half_length -1] + arr[half_length]) / 2
        return median
    else:
        median = arr[half_length]
        return median

#Take the input for both of the arrays
input_arr1 = input("Enter the elements of the first array separated by spaces: ")
elements1 = input_arr1.split()
input_arr2 = input("Enter the elements of the second array separated by spaces: ")
elements2 = input_arr2.split()

#Makes all of the elements a float
array_elements1 = [float(element) for element in elements1]
array_elements2 = [float(element) for element in elements2]

#Merge both of the arrays that were inputed 
merge_array = array_elements1 + array_elements2

merge_array.sort(reverse=False)

med_value = arr_median(merge_array)

print("The whole merged array entered by the user:", merge_array)
print("The median value of the array:", med_value)



