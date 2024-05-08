# This program will take a list of N number of elements.
# The list will hold all of the elements from 1 to N in no particular order.
# One number will be missing and it is up to the program to determine the missing number.
# For example, N = 5 input: [1, 2, 5, 4], output: 3
# HINT: N is the highest index + 1!!!!!

#define variables
i = 1
my_List = []

N = int(input("Input the maximum number you want in your list: "))
total_elements = N-1
print("Input the list with with a maximum of", total_elements, "elements all between 1 and",  N) 

#Going to take the list input 
while i < N:
    element = int(input("Input element that is less than N: "))
    if (element <= N) and (element not in my_List):
        my_List.append(element)
        print("pass")
        i = i+1
    else:
        print("Element not accepted please retry.")

#Sorts the elements in the list from smallest to largest
sorted_list = my_List.sort(reverse=False)

#Logic to find missing element
list_sum = N * (N + 1) // 2 #Takes sum of list with N elements
actual_sum = sum(my_List)

missing_num = int(list_sum - actual_sum)

print("The missing number in the list is :", missing_num)



   