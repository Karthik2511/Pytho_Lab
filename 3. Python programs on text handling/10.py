#translate and maketrans
# The maketrans() method returns a mapping table that can be used with the translate() method to replace characters
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(mytable) # prints a mapping table with ascii values
# ------------------------------------------------------------------------
# The translate() method returns a string where some specified characters are replaced with the character described in the dictionary or in the mapping table
# If a character is not specified in the dictionary/table, the character will not be replaced.
# If you use a dictionary, you must use ascii codes instead of characters
print(txt.translate(mytable)) # replace any character 'S' with a 'P' using a mapping table
# or
mydict = {83: 80}
print(txt.translate(mydict)) # replace any character 'S' with a 'P' using a dictionary
# ------------------------------------------------------------------------
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y) # create a mapping table
mytable.update({ord(char): None for char in z}) # remove characters in z from the string
print(txt.translate(mytable))