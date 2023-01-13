alphabet = 'abcdefghijklmnopqrstuvwxyz'

# First half of alphabet
print(alphabet[0:len(alphabet) // 2])

# First half using ending index
print(alphabet[:len(alphabet) // 2])

# Second half of string using ending index
alphabet[len(alphabet) // 2:len(alphabet)]

#Second half using starting and ending
alphabet[len(alphabet) // 2:len(alphabet)]

#Second half using starting
alphabet[len(alphabet) // 2:]

# Every second letter in the string starting with 'a'.
alphabet[::2]

# The entire string in reverse. 
alphabet[::-1]

# Every third letter of the string in reverse starting with 'z'.
alphabet[::-3]