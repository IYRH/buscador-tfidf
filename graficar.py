import matplotlib.pyplot as plt
import squarify 
from nltk.corpus import stopwords
from collections import Counter

def palabras_mas_comunes(n, archivo):
	palabras = []

	with open(archivo) as fname:
		for linea in fname:
			palabras.extend(linea.split())
	reducida = [item for item in palabras if item not in stopwords.words('english')]
	return (Counter(reducida).most_common(n))

print (palabras_mas_comunes(17, 'Corpus-Med500.txt'))

frecuentes = [('growth', 249), ('patients', 210), ('may', 179), ('cells', 174), ('hormone', 168), ('normal', 156), ('children', 138), ('found', 134), ('treatment', 131), ('human', 130), ('cases', 130), ('one', 120), ('cell', 113), ('blood', 109), ('effect', 107)]

sizes = []
label = []

for x in frecuentes:
    sizes.append(x[1])
    label.append(x[0])

squarify.plot(sizes=sizes, label=label, alpha=0.6 )

plt.show()


