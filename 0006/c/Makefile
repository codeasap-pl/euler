.PHONY: clean slow fast
.NOTPARALLEL: clean

CFLAGS ?= -Wall -Wextra -pedantic -O2 -lm
INCLUDES = -I./

all: clean build

clean:
	rm -rfv prog.bin

build:
	cc $(CFLAGS) $(INCLUDES) -o prog.bin main.c
