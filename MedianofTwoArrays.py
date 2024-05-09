#This program will look at arrays of a variable size and get the median number of the two arrays. 
#Example [1, 2, 4], [3, 5, 4] = [1, 2, 3, 4, 4, 5], Median is 3.5

import array as arr

#Take the input for both of the arrays
input_arr1 = input("Enter the elements of the first array separated by spaces: ")
elements1 = input_arr1.split()
input_arr2 = input("Enter the elements of the second array separated by spaces: ")
elements2 = input_arr2.split()

#Makes all of the elements a float
array_elements1 = [float(element) for element in elements1]
array_elements2 = [float(element) for element in elements2]

#Sort the arrays from smallest number to biggest number.
array_elements1.sort(reverse=False)
array_elements2.sort(reverse=False)

print("The first array entered by the user:", array_elements1)
print("The second array entered by the user:", array_elements2)



