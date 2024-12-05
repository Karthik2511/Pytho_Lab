# working of read() mode
file=open('abc.txt','r')
print(file.read()) #prints entire file
file.seek(0)
print(file.read(5))