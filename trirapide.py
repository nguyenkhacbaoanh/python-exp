def qsort(l):
	if l == []: return []
	pivot, g, d = l[0], [], []
	for x in l[1:]:
		if (x<pivot): g.append(x)
		else: d.append(x)
	return (qsort(g)+[l[0]]+qsort(d))

import random as rd
import timeit as ti
list_init=rd.sample(range(100),10)
list_trie=qsort(list_init)
print(list_init)	
print(list_trie)
