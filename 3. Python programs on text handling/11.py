#some other string functions
txt = "My name is Ståle"
x = txt.encode() #1. encode() method encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
print(x)
# ------------------------------------------------------------------------
txt = 'h\te\tl\tl\t0'
x = txt.expandtabs(1) #2. the expandtabs() method sets the tab size to the specified number of white spaces
print(x)
# ------------------------------------------------------------------------
txt = 'Demo'
print(txt.isidentifier()) #3. the isidentifier() method returns True if the string is an identifier, otherwise False
# ------------------------------------------------------------------------
print(txt.isprintable()) #4. the isprintable() method returns True if all the characters in string are printable,
# otherwise False
# ------------------------------------------------------------------------
txt = " "
print(txt.isspace()) #5. the isspace() method returns True if all the characters in a string are whitespaces,
# otherwise False
# ------------------------------------------------------------------------
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple) #6. the join method() takes all items in an iterable and joins them into one string.
# A string must be specified as a seperator
print(x)
# ------------------------------------------------------------------------
txt = "50"
print(txt.zfill(10)) #7. the zfill() method adds zeros to a string, until it reaches the specified length
# ------------------------------------------------------------------------
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines()) 
#8. the splitlines() method splits a string into a list. The splitting is done at line breaks