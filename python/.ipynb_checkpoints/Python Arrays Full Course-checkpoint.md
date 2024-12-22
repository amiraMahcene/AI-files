# Python Arrays: Full Course

# Introduction
# In Python, an array is a data structure that can hold multiple elements of the same type. 
# Arrays are part of the `array` module and should not be confused with Python lists.

import array

# Creating Arrays
# Arrays are created using the `array` module:
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' denotes integer type
print("Array elements:", arr)

# Accessing Array Elements
# Elements can be accessed using their index:
print("First element:", arr[0])  # Accessing the first element

# Adding Elements
# Use `append()` or `extend()` to add elements:
arr.append(6)  # Adding a single element
print("Array after append:", arr)

arr.extend([7, 8, 9])  # Adding multiple elements
print("Array after extend:", arr)

# Inserting Elements
# Use `insert()` to add elements at a specific index:
arr.insert(2, 10)  # Insert 10 at index 2
print("Array after insert:", arr)

# Removing Elements
# Use `remove()` or `pop()` to remove elements:
arr.remove(10)  # Removes the first occurrence of 10
print("Array after remove:", arr)

removed_element = arr.pop(3)  # Removes and returns the element at index 3
print("Removed element:", removed_element)
print("Array after pop:", arr)

# Slicing Arrays
# Arrays can be sliced like lists:
slice_arr = arr[1:4]  # Slice from index 1 to 3
print("Sliced array:", slice_arr)

# Iterating Through Arrays
# You can use loops to iterate over arrays:
for element in arr:
    print("Element:", element)

# Array Methods
# Some useful methods include:
print("Count of 2 in array:", arr.count(2))  # Counts occurrences of 2
print("Index of 7:", arr.index(7))  # Finds the first index of 7

# Array Operations
# Arrays support basic arithmetic operations:
arr2 = array.array('i', [10, 20, 30])
concatenated = arr + arr2  # Concatenation
print("Concatenated array:", concatenated)

# Array Copying
# Use slicing to create a copy of an array:
copied_arr = arr[:]
print("Copied array:", copied_arr)

# Sorting Arrays
# Use Python's `sorted()` function or manually sort:
sorted_arr = array.array('i', sorted(arr))
print("Sorted array:", sorted_arr)

# Reversing Arrays
# Use slicing or the `reverse()` method:
arr.reverse()
print("Reversed array:", arr)

# Array Buffer Interface
# Use the buffer interface for advanced operations:
buffer = memoryview(arr)
print("Buffer representation:", buffer.tolist())

# Multidimensional Arrays
# Python arrays are one-dimensional; use `numpy` for multidimensional arrays.
import numpy as np
multi_arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Multidimensional array:\n", multi_arr)

# Exercises
# 1. Create an array of floats and perform operations similar to the above.
# 2. Write a function that takes an array and returns a new array with elements doubled.
# 3. Use slicing to reverse an array without using the `reverse()` method.

# Summary
# - Arrays are efficient for storing and manipulating data of the same type.
# - The `array` module is used for one-dimensional arrays.
# - For advanced operations, consider using libraries like `numpy`.

# Python Lists: Full Course

# Introduction
# A list is a built-in Python data structure that can hold a collection of items, which can be of different types.

# Creating Lists
# Lists are created using square brackets []:
my_list = [1, 2, 3, 4, 5]
print("List elements:", my_list)

# Lists can hold mixed types of data:
mixed_list = [1, "hello", 3.14, True]
print("Mixed type list:", mixed_list)

# Accessing List Elements
# Elements can be accessed using their index (starting from 0):
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Modifying List Elements
# Lists are mutable, so elements can be updated:
my_list[0] = 10
print("Updated list:", my_list)

# Adding Elements
# Use `append()` to add a single element at the end:
my_list.append(6)
print("List after append:", my_list)

# Use `extend()` to add multiple elements:
my_list.extend([7, 8, 9])
print("List after extend:", my_list)

# Use `insert()` to add an element at a specific index:
my_list.insert(2, 15)  # Insert 15 at index 2
print("List after insert:", my_list)

# Removing Elements
# Use `remove()` to delete the first occurrence of a value:
my_list.remove(15)
print("List after remove:", my_list)

# Use `pop()` to remove an element by index (and return it):
removed_element = my_list.pop(3)  # Removes the element at index 3
print("Removed element:", removed_element)
print("List after pop:", my_list)

# Use `clear()` to remove all elements:
copy_list = my_list[:]
copy_list.clear()
print("Cleared list:", copy_list)

# Slicing Lists
# Use slicing to extract portions of a list:
slice_list = my_list[1:4]  # Slice from index 1 to 3
print("Sliced list:", slice_list)

# Iterating Through Lists
# Use loops to iterate over lists:
for element in my_list:
    print("Element:", element)

# List Comprehension
# A concise way to create lists:
squares = [x**2 for x in range(1, 6)]
print("Squares list:", squares)

# Searching in Lists
# Use `in` to check for membership:
print("Is 3 in the list?", 3 in my_list)

# Use `index()` to find the position of an element:
if 3 in my_list:
    print("Index of 3:", my_list.index(3))

# Sorting Lists
# Use `sort()` to sort in place:
unsorted_list = [5, 2, 9, 1]
unsorted_list.sort()
print("Sorted list:", unsorted_list)

# Use `sorted()` to return a new sorted list:
reversed_sorted = sorted(unsorted_list, reverse=True)
print("Reversed sorted list:", reversed_sorted)

# Reversing Lists
# Use `reverse()` to reverse in place:
unsorted_list.reverse()
print("Reversed list:", unsorted_list)

# Use slicing to reverse:
reversed_list = my_list[::-1]
print("Reversed list using slicing:", reversed_list)

# Copying Lists
# Use slicing or the `copy()` method to create a copy:
copy1 = my_list[:]
copy2 = my_list.copy()
print("Copy using slicing:", copy1)
print("Copy using copy():", copy2)

# Nested Lists
# Lists can contain other lists:
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)
print("Accessing nested element:", nested_list[1][1])  # Accessing 4

# Common List Methods
# len(), max(), min(), sum()
print("Length of list:", len(my_list))
print("Max element:", max(my_list))
print("Min element:", min(my_list))
print("Sum of elements:", sum(my_list))

# Exercises
# 1. Create a list of numbers and find the largest and smallest elements.
# 2. Write a function that takes a list and returns a new list with unique elements.
# 3. Reverse a list without using slicing or the `reverse()` method.

# Summary
# - Lists are versatile and easy to use for storing and manipulating collections of data.
# - They are mutable, allowing for dynamic updates.
# - Python provides a rich set of methods and functionalities for working with lists.




