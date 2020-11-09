all: memory_thing memory_thing2

memory_thing: memory_thing.c
	gcc -Wall -o memory_thing memory_thing.c -static

memory_thing2: memory_thing.c
	gcc -Wall -o memory_thing2 memory_thing.c

clean:
	rm -f memory_thing memory_thing2
