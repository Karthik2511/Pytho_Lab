#align a string
txt = "hello"
# the center() method will align the string, using a specified character(space is default) as the fill character
# syntax: string.center(length,character)...length=Required. The length of the returned string
# character=Optional. The character to fill the missing space on each side.
# Default is " "(space).
a = txt.center(20)
print(a)
# with fill character as "0"
a = txt.center(20, '0')
print(a)
print(len(a))
# -------------------------------------------------------------------------
# the ljust() method will left align the string, using a specified character as the fill character with
# the specified length
a = txt.ljust(20, "*")
print(a, "world")
# -------------------------------------------------------------------------
# the rjust() method will right align the string, using a specified character as the fill character with
# the specified length
a = txt.rjust(20, "*")
print(a)
