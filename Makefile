SRCDIR = src
TSTDIR = test

THETA = thetas.npy

.SILENT:

all:
	python3 $(SRCDIR)/train.py $(TSTDIR)/data.csv \
	&& printf "\x1B[32m Model Trained!\x1B[0m\n" || true

e:
	python3 $(SRCDIR)/estimate.py || true

t:
	python3 $(TSTDIR)/gencsv.py
	python3 $(SRCDIR)/train.py $(TSTDIR)/line.csv

clean:
	rm -rf $(TSTDIR)/line.csv

fclean: clean
	rm -rf $(THETA)

gpush: fclean
	git add .
	git commit -m "axislabels"
	git push

re: fclean all
