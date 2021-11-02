import csv

with open('dados.m', newline='\n') as csvfile:
	data = list(csv.reader(csvfile, delimiter=','))
	#for row in reader:
		#print(', '.join(row))
	print (data)
