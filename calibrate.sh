!$/bin/bash

echo "enter filename for data: "
read POS 				#calibration data is written to POS file


for index in 1 .. 5
do
	echo "press enter once in position "
	read

	#writes to file
	if [ $index == 1 ]
	then
	./myo_collect > $POS &
	else
	./myo_collect >> $POS &
	fi

	PID=$!
	sleep 1
	echo -n "calibrating"

	for N in 1 .. 4
	do
	    sleep 1 && echo -n "."
	done
	
	#ends calibration if small amount of data
	#only covers first calibration malfunction
	lines = wc -l $POS
	if [ $lines -lt 10 ] 
	then
		echo "There was a problem getting data from the Myo"
		echo "Resync the device and try calibrating again"			
		break
	fi

	sleep 1
	kill $PID #silence

	echo "rest your arm"
	sleep 3
	echo
done
