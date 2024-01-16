fruit = ["apple","guava","orange","grapes","kiwi"]
#map
cap_words = list(map(lambda x: x.upper(),fruit))
print("Cap_Words:" , cap_words)

#Filter
g_words = list(filter(lambda x:x.startswith("g"),fruit))
print("G_Words:" , g_words)

#reduce
from functools import reduce

s = reduce(lambda x,y: x+y, fruit)
print(s)
