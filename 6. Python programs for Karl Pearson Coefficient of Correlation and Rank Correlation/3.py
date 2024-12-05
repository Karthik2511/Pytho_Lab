#calculating rank correlating using scipy.stats
import scipy.stats
x = [15,18,21, 15, 21]
y = [25,25,27,27,27]
print(scipy.stats.spearmanr(x, y)[0])