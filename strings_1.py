#Advanced concepts - strings

message = ' Hello, World! '

print(message[0])
print(message[1:4])  # prints 'ell'
print(message[1:])   # prints 'ello'
print(message[-1])   # prints 'o'

print(len(message))  # prints 5
print(message.upper())  # prints 'HELLO'
print(message.lower())  # prints 'hello'
print(message.replace('h', 'H'))  # prints 'Hello'
print(message.strip())  # removes whitespace from both ends, prints 'hello'
print(message.split(','))