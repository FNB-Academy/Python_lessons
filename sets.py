#Sets
'''
my_set = {1,2,3,4,5}

print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)  # Add an item to the set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)  # Remove an item from the set
print(my_set)  # Output: {1, 2, 4, 5, 6}

'''
# Sets in Python

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union of sets(removes duplicates)
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# intersection of sets(common elements)
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# difference of sets(elements in set1 but not in set2)
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}