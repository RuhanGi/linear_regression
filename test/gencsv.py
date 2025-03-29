import csv
import random

def generate_data(n, filename):
	with open(filename, mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['km', 'price'])
		r = 0.2
		for x in range(n):
			y = (-0.021 * (x * 2000) + 8500) * random.uniform(1-r, 1+r)
			writer.writerow([(x * 2000), y])

n = 120
filename = "test/line.csv"

generate_data(n, filename)
