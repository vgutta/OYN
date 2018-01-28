#!/bin/bash

for POS in dab.pos please.pos thanks.pos hi.pos time.pos
do
    echo $POS
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
		sleep 0.5
		echo -n "calibrating"
	
		for N in 1 .. 4
		do
		    sleep 0.5 && echo -n "."
		done
                echo
                
		sleep 0.5
		kill $PID
                wait $PID 2>/dev/null
	
		echo "rest your arm"
		sleep 3
		echo
	done

done
