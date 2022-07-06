.NOTPARALLEL: clean

CFLAGS ?=


all: clean build

clean:
	rm -rfv prog

build:
	cc main.c -Wall -Wextra -pedantic -O1 -o prog -lm


profile:
	gcc main.c -Wall -Wextra -pedantic -pg -o prog -lm
	./prog 123123123
	gprof -b prog gmon.out
