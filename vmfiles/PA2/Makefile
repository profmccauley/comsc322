# First target is the default if you just say "make"
all: make_random uniq_ints

make_random: make_random.c
	gcc -g -Wall -o make_random make_random.c

uniq_ints: uniq_ints.c
	gcc -g -Wall -o uniq_ints uniq_ints.c

test_make_random: make_random
	./test_make_random.py -v

test_uniq_ints: uniq_ints
	./test_uniq_ints.py -v

tests: all
	python3 -m unittest test_make_random.py test_uniq_ints.py

clean:
	rm -f make_random uniq_ints
