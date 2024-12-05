#Calculating mode
ls2 = [3,15,23,42,30,10,10,12]
ls3 = ['nike','adidas','nike','jordan','jordan','rebook','under_amour','adidas']
def mode(dataset):
	frequency = {}
	for value in dataset:
		frequency[value] = frequency.get(value,0)+1
	most_frequent = max(frequency.values())
	modes = [key for key,value in frequency.items() if value == most_frequent]
	return modes
print(mode(ls2))
print(mode(ls3))