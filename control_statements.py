#control statements

#/num = 0

#if(num > 0):
#   print("This number is positive.")
#elif(num == 0):
#    print("This number is zero.")
#else:
#    print("This number is negative.")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter second  number: "))

if num1 > num2:
    print(num1, " is greater than ", num2)
elif num1 < num2:
    print(num1, " is less than ", num2)
else:
    print("Both numbers are equal.")