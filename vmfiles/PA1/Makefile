# First target is the default if you just say "make"
all: sizes cards tokenize

sizes: sizes.c
	gcc -g -Wall -o sizes sizes.c

cards: cards.c
	gcc -g -Wall -o cards cards.c

tokenize: tokenize.c
	gcc -g -Wall -o tokenize tokenize.c

test_sizes: sizes
	./test_sizes.py -v

test_tokenize: tokenize
	./test_tokenize.py -v

test_cards: cards
	./test_cards.py -v

tests: all
	python3 -m unittest test_sizes.py test_tokenize.py test_cards.py

clean:
	rm -f sizes cards tokenize
