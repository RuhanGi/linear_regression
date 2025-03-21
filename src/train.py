import numpy as np
import sys
import csv

RED = "\033[91m"
RESET = "\033[0m"

if len(sys.argv) != 2:
	print(RED + "Pass Training Data!" + RESET)
	sys.exit()

def load():
	try:
		theta0, theta1 = np.load("thetas.npy")
		return theta0, theta1
	except:
		print(RED + "Improper training file!" + RESET)
		sys.exit()

th0, th1 = load()

def epoch(fil):
	global th0, th1
	learningRate = 0.05
	try:
		with open(fil) as file:
			csvFile = csv.reader(file)
			fields = next(csvFile)
			if fields[0] != "km" or fields[1] != "price":
				raise 
			m = 0
			s1 = 0
			s2 = 0
			for lines in csvFile:
				m += 1
				s1 += (th0 + th1 * float(lines[0])) - float(lines[1])
				s2 += ((th0 + th1 * float(lines[0])) - float(lines[1])) * float(lines[0])
			th0 -= learningRate * s1 / m
			th1 -= learningRate * s2 / m
	except:
		print(RED + "Improper Training Data!" + RESET)
		sys.exit()

tolerance = 0.0001
prvth0, prvth1 = th0, th1
epoch(sys.argv[1])
print(f"theta0: {prvth0}, theta1: {prvth1}")
while (abs(th0 - prvth0) > tolerance) or (abs(th1 - prvth1) > tolerance):
	prvth0, prvth1 = th0, th1
	epoch(sys.argv[1])
	print(f"theta0: {prvth0}, theta1: {prvth1}")
np.save("thetas.npy", np.array([th0, th1]))
