#slicing a string
string = "Hello World"
# Get the characters from position 2 to position 5 (not included)
print(string[2:5])
# ------------------------------------------------------------------------
# slice from the start until position 5 (not included)
print(string[:5])
# ------------------------------------------------------------------------
# slice until the end from position 2
print(string[2:])
# ------------------------------------------------------------------------
# using negative indexes to slice from position -5 (not included) to -2
print(string[-5:-2])
