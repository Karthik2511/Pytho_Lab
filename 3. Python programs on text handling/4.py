#format strings
age = 18
# we cannot combine text and numbers like this
txt = "My name is John, and my age is " + str(age)
# instead we use the format() method which takes the passed arguments, formats them,
# and places them in the string where the placeholders {} are:
txt = "My name is John, and I am {}"
print(txt.format(age))
# -------------------------------------------------------------------------
# format() method takes unlimited arguments and places it in respective placeholders{}
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# -------------------------------------------------------------------------
# we can also use index numbers to be sure the arguments are placed in correct placeholders
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))