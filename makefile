CC = g++
DIR = $(shell pwd)
CPPFLAGS = -F $(DIR) -framework myo -rpath @loader_path
EXEC = demo

all:
	$(CC) $(CPPFLAGS) demo.cpp -o $(EXEC)
