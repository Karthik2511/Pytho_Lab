# Program 6 :- Using mode() & multimode from statistics module
from statistics import mode,multimode
ls2 = [3,15,23,42,30,10,10,12]
ls3 = ['nike','adidas','nike','jordan','jordan','reebok','under_amour','adidas']
print(mode(ls2))
print(mode(ls3))
print(multimode(ls2))
print(multimode(ls3))