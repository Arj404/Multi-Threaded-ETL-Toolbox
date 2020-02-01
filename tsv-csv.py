file = open("auto-data","r")
export = open("export-data.csv","w")
f=0
s=0
for line in file:
	for word in line:
			if(" " == word and f == 0 and s==0):
				export.write(",")
				f=1
			elif(" " == word and f == 1 and s==0):
				continue
			elif("\t"==word and s==0):
				export.write(",")
			else:
				f=0
				if("\"" == word):
					if(s==1):
						s=0
					else:
						s=1
				export.write(word)
file.close()
export.close()