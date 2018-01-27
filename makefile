CC = g++
DIR = $(shell pwd)
CPPFLAGS = -F $(DIR) -framework myo -rpath @loader_path
EXEC = myo_collect

all:
	$(CC) $(CPPFLAGS) myo_collect.cpp -o $(EXEC)
