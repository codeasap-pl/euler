.PHONY: clean slow fast
.NOTPARALLEL: clean

CFLAGS ?= -Wall -Wextra -pedantic -O2 -lm
INCLUDES = -I./

all: clean build

clean:
	rm -rfv slow.bin fast.bin

build: slow fast

slow:
	cc $(CFLAGS) $(INCLUDES) -DSLOW -o slow.bin \
		main.c slow/slow.c

fast:
	cc $(CFLAGS) $(INCLUDES) -DFAST -o fast.bin \
		main.c fast/fast.c fast/vector/vector.c
