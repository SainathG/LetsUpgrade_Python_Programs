str1='hyderabad ts'
str1[2:]
print(str1.islower())                 # Check the given string contains only lowers  case

print(str1.find('s', 0, len(str1)))   # To find the given substring start position in given string

print(str1.__contains__('b'))         # checks whether  letter/substring exist or not  in string

print(str1[2:])                       # Slice the to end

print(str1.strip())                   # Removes any whitespace from the beginning or the end

print (str1.title())                  # Converts the first character of each word to upper case
