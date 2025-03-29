import matplotlib.pyplot as plt
import numpy as np
import sys
import csv

RED = "\033[91m"
RESET = "\033[0m"

def rmse(act, prd):
	assert len(act) == len(prd), "Length mismatch between actual and predicted values."
	return np.sqrt(np.mean((act - prd) ** 2))

def mae(act, prd):
	assert len(act) == len(prd), "Length mismatch between actual and predicted values."
	return np.mean(np.abs(act - prd))

def rsqr(act, prd):
	assert len(act) == len(prd), "Length mismatch between actual and predicted values."
	mean_act = np.mean(act)
	sse = np.sum((act - prd) ** 2)
	tss = np.sum((act - mean_act) ** 2)
	return 1 - (sse / tss) if tss != 0 else 0

def r(x, y):
	assert len(x) == len(y), "Length mismatch between x and y values."
	meanx, meany = np.mean(x), np.mean(y)
	num = np.sum((x - meanx) * (y - meany))
	den = np.sqrt(np.sum((x - meanx) ** 2) * np.sum((y - meany) ** 2))
	return num / (den) if den != 0 else 0

def normalize(data):
	return (data - np.min(data)) / (np.max(data) - np.min(data))

def plot(data, th0, th1):
	try:
		kms, prices = data[:, 0], data[:, 1]
		predictions = th0 + th1 * kms

		fig, ax = plt.subplots()
		ax.scatter(kms, prices, color='red', label="Data")
		ax.plot(kms, predictions, color='blue', label="Regression Line")
		plt.text(min(kms)+0.75*(max(kms)-min(kms)), min(prices)+0.8*(max(prices)-min(prices)), 
					f"Precision:\n"
					f"- RMSE = {rmse(prices, predictions):.2f}\n"
					f"- MAE = {mae(prices, predictions):.2f}\n"
					f"- R² = {rsqr(prices, predictions):.4f}", color = 'blue')
		plt.text(min(kms)+0.2*(max(kms)-min(kms)), min(predictions)+0.3*(max(predictions)-min(predictions)), 
					f"y = ({th0:.2f}) + ({th1:.4g})x", color = 'blue')
		plt.text(min(kms)+0.1*(max(kms)-min(kms)), min(prices)+0.1*(max(prices)-min(prices)), 
					f"Correlation:\nr = {r(kms, prices):.4f}", color = 'red')
		plt.xlabel("Mileage (km)")
		plt.ylabel("Price")
		plt.title("Trained Data")
		def on_key(event):
			if event.key == "escape":
				plt.close(fig)
		fig.canvas.mpl_connect("key_press_event", on_key)
		plt.show()
	except Exception as e:
		print(RED + "Error in Plotting: " + str(e) + RESET)
		sys.exit(1)

def loadData(fil):
	try:
		return np.loadtxt(fil, delimiter=",", skiprows=1)
	except Exception as e:
		print(RED + "Error: " + str(e) + RESET)
		sys.exit(1)

def epoch(nkms, nprices, th0, th1):
	learningRate = 0.6
	npredictions = th0 + th1 * nkms
	m = len(nkms)
	tmp0 = learningRate * np.sum(npredictions - nprices) / m
	tmp1 = learningRate * np.sum((npredictions - nprices) * nkms) / m
	return th0 - tmp0, th1 - tmp1

def trainModel(data, th0, th1):
	try:
		kms, prices = data[:, 0], data[:, 1]
		nkms, nprices = normalize(kms), normalize(prices)
		maxiterations = 1000
		tolerance = 10**-6

		while True:
			prvth0, prvth1 = th0, th1
			th0, th1  = epoch(nkms, nprices, th0, th1)
			maxiterations -= 1
			if (abs(th0-prvth0) < tolerance and abs(th1-prvth1) < tolerance) or maxiterations == 0:
				break

		th1 = th1 * (np.max(prices) - np.min(prices)) / (np.max(kms) - np.min(kms))
		th0 = th0 * (np.max(prices) - np.min(prices)) + np.min(prices) - np.min(kms) * th1
		return th0, th1
	except Exception as e:
		print(RED + "Error: " + str(e) + RESET)
		sys.exit(1)

def main():
	if len(sys.argv) != 2:
		print(RED + "Pass Training Data!" + RESET)
		sys.exit()
	data = loadData(sys.argv[1])
	th0, th1 = trainModel(data, 0, 0)
	plot(data, th0, th1)
	np.save("thetas.npy", np.array([th0, th1]))

if __name__ == "__main__":
	main()