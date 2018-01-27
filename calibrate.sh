#!bin/bash

echo "enter filename for data: "
read POS 				#calibration data is written to POS file


for index in 1 .. 5
do
	echo "press enter once in position "
	read

	#writes to file
	./myo_collect >> $POS &
	PID=$!
	sleep 1
	echo -n "calibrating"

	for N in 1 .. 4
	do
	    sleep 1 && echo -n "."
	done

	sleep 1
	kill $PID | /dev/null

	echo "rest your arm"
	sleep 3
	echo
done
