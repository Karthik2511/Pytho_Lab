a = "Hello world"
print(len(a)) #1. len() function returns the length of the string
print(a.count("l")) #2. count() method returns the number of times the specified value occurs in the string
print(a.startswith("H")) #3. returns a boolean value if the string starts with the specified value
print(a.endswith("l")) #4. returns a boolean value if the string end with the specified value
print(a.find("l")) #5. returns the index value of the first occurrence of the specified value else returns -1
print(a.rfind("l")) #6. returns the index value of the last occurrence of the specified value else returns -1
print(a.isalnum()) #7. returns True if all the values in the string are alphanumeric
print(a.isdigit()) #8. returns True if all the values in the string are digits
print(a.isalpha()) #9. returns True if all the values in the string are alphabets
print(a.islower()) #10. returns True if all characters in the string are lower case