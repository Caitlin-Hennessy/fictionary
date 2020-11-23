import csv

f = open("testwords")
r = csv.reader(f, delimiter="\t")
w = open("test1", "a")
w.write("{")

for row in r:
	if len(row) == 2:
		w.write(" \"{}\":\"{}\",".format(row[0], row[1]))

w.write("}")
w.close()