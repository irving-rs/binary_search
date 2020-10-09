#binary_search.py
#Date: 03/October/2020
#by irving-rs

#Description:
#Binary Search: Searches a number inside a list using the binary search algorithm.

#Details:
#The user will be asked how many elements want to be created following the expression y = n^2 + 2.
#The user will select a number and the program will return the position (index) on the list where that value is found.
#The program will inform the user if the numbered is not in the list.


#FUNCTIONS:
def binary_search_algorithm(y,x): #Searching method. Returns the index or -1 if the number is not found. Also returns the number of iterations.
    #y is the list.
    #x is the number to be found.
    low = 0
    high = len(y)
    i = 0 #Iteration counter.

    while low <= high:
        i +=1 #Increase the iteration counter.
        mid = (low+high)//2
        if y[mid] == x: #If the number was found.
            return mid, i
        elif x > y[mid]: #If the number is greater than the current element of y, then search in the upper half.
            low = mid + 1
        elif x < y[mid]: #If the number is minor than the current element of y, then search in the lower half.
            high = mid - 1
    else: #The number was not found.
        return -1, i


#PRESENTATION:
print("\nBINARY SEARCH:")
print("\nSearches a number inside a list using the binary search algorithm.\n")

#INSTRUCTIONS:
print("Fist step: A list will be created, you only need to indicate the number (n) of elements.")
print("           The list will follow the formula: y = n^2 + 2\n")
print("Second step: You will enter a number.\n")
print("Third step: If the number is in the list, the index would be returned. If not, the program will tell you.\n")

#BODY:
n = int(input("Select the number of elements in the array: "))

y = [i**2+2 for i in range(n)] #Creation of the list.

print("y = ", y) #Printing the list.

x = int(input("\nEnter the number you want to find: "))

index, i = binary_search_algorithm(y,x)

if index!=-1: #If the number was found.
    print("\nThe number", x, "was found in the position (index)", index, "after", i, "iterations.\n")
else: #If the number was not found.
    print("\nThe number", x, "was not found after", i, "iterations.\n")
