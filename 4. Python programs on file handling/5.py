# Split() using file handling
with open('abc.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
