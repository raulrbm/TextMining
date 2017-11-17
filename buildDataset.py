#Raul R Bander
#Carnet: 12-11285
#Luis C Diaz
#Carnet: 11-10293
#Mineria de datos
#crea el dataset

#Importaciones:
import os

dirname = "poscorp/"
dataSetFile = open("dataset.csv", "w")
dataSetFile.write("id;")
tags = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD",
 "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS",
 "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP",
 "WP$", "WRB"]
for i in tags:
	dataSetFile.write(i)
	dataSetFile.write(";")
dataSetFile.write("Class\n")
pr = 0
for i in range (1,4):
	filePath = dirname+str(i)
	files = os.listdir(filePath)
	for f in files:
		dataSetFile.write(f+";")
		for t in tags:
			wFile = open(filePath+"/"+f, "r")
			tIncidence = 0
			for line in wFile.readlines():
				tagcito = line.split(",")[2]
				tagcote = t+"\n"
				if tagcito == tagcote:
					tIncidence += 1
			dataSetFile.write(str(tIncidence))
			dataSetFile.write(";")		
			pr = 1
		dataSetFile.write(str(i)+"\n")