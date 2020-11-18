# First target is the default if you just say "make"
all: mhcsh

mhcsh: mhcsh.c
	gcc -g -Wall -o mhcsh mhcsh.c

fast-tests: all
	python3 -m unittest -v test_mhcsh.py

tests: all
	python3 -m unittest -v test_mhcsh_slow.py

clean:
	rm -f mhcsh
