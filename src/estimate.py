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
	print(GREEN + "Estimated Price is " + CYAN + f"${theta0 + theta1 * mileage:.2f}" + GREEN + "!" + RESET)

if __name__ == "__main__":
    main()