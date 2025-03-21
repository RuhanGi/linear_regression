SRCDIR = src

DATA = data.csv

THETA = thetas.npy

.SILENT:

all:
	python3 $(SRCDIR)/train.py $(DATA)
	printf "\x1B[32m Model Trained!\x1B[0m\n";
	# python3 $(SRCDIR)/estimate.py

clean:
	rm -rf 

fclean: clean
	rm -rf $(THETA)
	python3 $(SRCDIR)/start.py

re: fclean all
