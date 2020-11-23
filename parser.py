import csv

f = open("words")
r = csv.reader(f, delimiter="\t")
w = open("wordsjson", "a")
w.write("{")

for row in r:
	if len(row) == 2:
		w.write(" \"{}\":\"{}\",".format(row[0], row[1]))

w.write("}")
w.close()