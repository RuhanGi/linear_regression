import numpy as np
import sys

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
GRAY = "\033[97m"
BLACK = "\033[98m"
RESET = "\033[0m"

def load():
	try:
		theta0, theta1 = np.load("thetas.npy")
		return theta0, theta1
	except:
		print(RED + "Improper training file!" + RESET)
		sys.exit()

def get():
	try:
		return float(input(BLUE + "Mileage (km): " + YELLOW))
	except:
		print(RED + "Input a Number!" + RESET)
		sys.exit()

def main():
	theta0, theta1 = load()
	mileage = get()
	prediction = theta0 + theta1 * mileage
	if mileage < 0 or prediction < 0:
		print(RED + "Invalid Values!\n" + GREEN + "Regression Output: ")
	else:
		print(GREEN + "Estimated Price: ")
	print(CYAN + f"${prediction:.2f}" + RESET)

if __name__ == "__main__":
	main()