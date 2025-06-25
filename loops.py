#loops

#fruits = ['apple', 'banana', 'cherry']
#for fruit in fruits:
 #   print(fruit)
    
    
#numbers = [1, 2, 3, 4, 5, 7]
#for number in numbers:
 #  print(number)    
   
   
#while loop to count from 1 to 5
# This code uses a while loop to count from 1 to 5 and prints each number

#count = 1

#while count <= 5:
 #   print("Count is:", count)
   # count += 1  # Increment count by 1 each iteration

#loop Control Statements

# List of fruits
#fruits = ['apple', 'banana', 'cherry', 'date']

# Break statement example: stop the loop when 'cherry' is found
#for fruit in fruits:
#   if fruit == 'cherry':
#       break  # Exit the loop when 'cherry' is found
#   print("Fruit:", fruit)

#print()  

# Continue statement example: skip 'cherry' and continue with the next iteration
#for fruit in fruits:
 #   if fruit == 'cherry':
 #       continue  # Skip the rest of the loop when 'cherry' is found
 #   print("Fruit:", fruit)
    
#print()  

# Pass statement example: do nothing special when 'cherry' is found, just continue
#for fruit in fruits:
#    if fruit == 'cherry':
#        pass  # No operation; loop continues as normal
#    print("Fruit:", fruit)

count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        break  # Skip the rest of the loop when count is 3
    
    
