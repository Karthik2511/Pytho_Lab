#linear search
def search(arr, N, x):
	for i in range(0, N):
		if arr[i] == x:
			return i
	return -1

#driver code
if __name__ == '__main__':
	arr = [2, 3, 4, 10, 40]
	x = 10
	N = len(arr)
	result = search(arr, N, x)
	if result == -1:
		print("element is not present")
	else:
		print("element is present at index", result)