#lists

fruits = ["apple", "banana", "cherry"]

print(fruits[0])

fruits[1] = "blueberry"  # Change the second item
print(fruits)  # Output: blueberry

#add  items
fruits.append("orange")  # Add an item to the end of the list
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

#add value at a specific index
fruits.insert(1, "kiwi")  # Insert an item at index 1
print(fruits)  # Output: ['apple', 'kiwi', 'blueberry', 'cherry', 'orange']

#remove items
fruits.remove("kiwi")  # Remove an item by value
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

#sorting lists
fruits.sort()  # Sort the list in ascending order
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

#reverse the list
fruits.sort(reverse=True)  # Sort the list in descending order
print(fruits)  # Output: ['orange', 'cherry', 'blueberry', 'apple']

