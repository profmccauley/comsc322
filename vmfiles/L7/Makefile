all: basic_fork fork_and_sleep fork_and_increment forks_upon_forks exec_and_wait

basic_fork: basic_fork.c
	gcc -g -Wall -o basic_fork basic_fork.c

fork_and_sleep: fork_and_sleep.c
	gcc -g -Wall -o fork_and_sleep fork_and_sleep.c

forks_upon_forks: forks_upon_forks.c
	gcc -g -Wall -o forks_upon_forks forks_upon_forks.c

fork_and_increment: fork_and_increment.c
	gcc -g -Wall -o fork_and_increment fork_and_increment.c

exec_and_wait: exec_and_wait.c
	gcc -g -Wall -o exec_and_wait exec_and_wait.c

clean:
	rm -f basic_fork fork_and_sleep fork_and_increment forks_upon_forks exec_and_wait
