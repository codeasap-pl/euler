.PHONY: clean slow fast
.NOTPARALLEL: clean

all: clean build

clean:
	rm -rfv prog.bin

build:
	cc -Wall -Wextra -pedantic -O2 main.c -o prog.bin -lm
