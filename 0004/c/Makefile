.NOTPARALLEL: clean

CFLAGS ?=

ifeq ($(DEBUG),1)
	CFLAGS += -DDEBUG
endif


all: clean build

clean:
	rm -rfv prog

build:
	cc $(CFLAGS) main.c -Wall -Wextra -pedantic -O2 -o prog -lm
