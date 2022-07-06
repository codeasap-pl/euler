.NOTPARALLEL: clean

CFLAGS ?=


all: clean build

clean:
	rm -rfv prog

build:
	cc main.c -Wall -Wextra -pedantic -O1 -o prog -lm
