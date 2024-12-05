# calculating median
ls2 = [187, 187, 196, 196, 198, 203, 207, 211, 215]
ls3 = [181, 187, 196, 198, 203, 207, 211, 215]

def median(dataset):
	data = sorted(dataset)
	index = len(data) // 2
	if len(dataset) % 2 != 0:
		return data[index]
	return (data[index - 1] + data[index]) / 2

print(median(ls2))
print(median(ls3))