file = open("export-data.csv","r")
export = open("export-data-c.csv","w")
for line in file:
	if("?" in line):
		continue
	else:
		export.write(line)
file.close()
export.close()