SRCDIR = src

DATA = data.csv

THETA = thetas.npy

.SILENT:

all:
	python3 $(SRCDIR)/train.py $(DATA)
	printf "\x1B[32m Model Trained!\x1B[0m\n";
	# python3 $(SRCDIR)/estimate.py

e:
	python3 $(SRCDIR)/estimate.py

clean:
	

fclean: clean
	rm -rf $(THETA)

re: fclean all
