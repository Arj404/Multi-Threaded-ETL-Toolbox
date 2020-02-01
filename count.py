file1 = open("export-data.csv","r")
file2 = open("export-data-c.csv","r")
c=0
for line in file1:
	c=c+1
print(c)
c=0
for line in file2:
	c=c+1
print(c)