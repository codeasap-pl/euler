.PHONY: clean
.NOTPARALLEL: clean

CFLAGS ?= -Wall -Wextra -pedantic -O2
INCLUDES = -I./

all: clean build

clean:
	rm -rfv prog.bin

build:
	cc $(CFLAGS) $(INCLUDES) -o prog.bin main.c
