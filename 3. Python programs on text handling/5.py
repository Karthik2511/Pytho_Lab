#looping in strings
a = "Hello"
for x in a:
 print(x)
# another way of writing the above program...
for x in "Hello":
 print(x)
# to avoid printing a new line everytime a print statement is called...
for x in a:
 print(x, end="")
