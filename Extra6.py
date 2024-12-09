#write a program nthat computer the total size of all the files in a directory
import os

def get_total_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

directory = 'C:/Users/karth/Desktop'
print(f"Total size: {get_total_size(directory)} bytes")