#Raul R Bander
#Carnet: 12-11285
#Luis C Diaz
#Carnet: 11-10293
#Mineria de datos
#POS TAGGER - Formato TF-IDF

#Importaciones:
import nltk
import os

#Funcion que genera el POS tag de una oracion
def tag(s):
	t = nltk.word_tokenize(s)
	return nltk.pos_tag(t)

#Funcion que abre un archivo y devuelve su contenido
def gettext(f):
	fl = open(f,'r')
	txt = ""
	for line in fl.readlines():
		txt = txt + line + "\n"
	return txt


#Funcion que escribe un archivo con el resultado del pos tag
def wpos(f,s):
	fl = open(f,'w')
	fl.write(s)

#Escribimos la primera linea del csv
st = "Doc_ID,TAGS,CLASS\n"

#Genera una lista con los archivos de la carpeta 1
dirname = "corp/1"
fls = os.listdir(dirname)
i = 0
for f in fls:
	#Guardamos el id del texto
	i = i + 1
	#Obtenemos los tags para f
	tags = tag(gettext("corp/1/" + f))
	#Creamos un dicionario con los tags obtenidos
	d = dict(tags)
	#Creamos un string auxiliar con los tags que contenia el texto
	aux0 = gettext("corp/1/" + f).split(" ")
	aux = ""
	for w in aux0:
		try:
			aux = aux + d[w] + ","
		except KeyError:
			aux = aux
	#Escribimos la linea en el csv
	aux = aux [:-1]
	st = st + str(i) + ",\"" + aux + "\",1\n"

#Genera una lista con los archivos de la carpeta 2
dirname = "corp/2"
fls = os.listdir(dirname)
for f in fls:
	#Guardamos el id del texto
	i = i + 1
	#Obtenemos los tags para f
	tags = tag(gettext("corp/2/" + f))
	#Creamos un dicionario con los tags obtenidos
	d = dict(tags)
	#Creamos un string auxiliar con los tags que contenia el texto
	aux0 = gettext("corp/2/" + f).split(" ")
	aux = ""
	for w in aux0:
		try:
			aux = aux + d[w] + ","
		except KeyError:
			aux = aux
	#Escribimos la linea en el csv
	aux = aux [:-1]
	st = st + str(i) + ",\"" + aux + "\",2\n"

#Genera una lista con los archivos de la carpeta 3
dirname = "corp/3"
fls = os.listdir(dirname)
for f in fls:
	#Guardamos el id del texto
	i = i + 1
	#Obtenemos los tags para f
	tags = tag(gettext("corp/3/" + f))
	#Creamos un dicionario con los tags obtenidos
	d = dict(tags)
	#Creamos un string auxiliar con los tags que contenia el texto
	aux0 = gettext("corp/3/" + f).split(" ")
	aux = ""
	for w in aux0:
		try:
			aux = aux + d[w] + ","
		except KeyError:
			aux = aux
	#Escribimos la linea en el csv
	aux = aux [:-1]
	st = st + str(i) + ",\"" + aux + "\",3\n"

wpos("tfidf.csv",st)