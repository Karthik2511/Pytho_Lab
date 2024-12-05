# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# ------------------------------------------------------------------------
# If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole
# string, 2 - an empty string, 3 - an empty string
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)

# ------------------------------------------------------------------------
# The rpartition() method searches for the last occurrence of a specified string, and splits the string
# into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
