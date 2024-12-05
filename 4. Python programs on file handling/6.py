# with block
with open('abc.txt') as file:
 data = file.read()
 print(data)
#no need to use close() in with block