#!/bin/bash

REST=rest.pos

echo "enter filename: "
read POS

echo "press enter once in position "
read

./myo_collect > $POS &
PID=$!
sleep 1 && echo -n "calibrating"

for N in 1 .. 4
do
    sleep 1 && echo -n "."
done

echo

sleep 1 && kill $PID | /dev/null


echo "press enter when in resting position"
read

./myo_collect > $REST &
PID=$!
sleep 1 && echo -n "calibrating"

for N in 1 .. 4
do
    sleep 1 && echo -n "."
done

echo

sleep 1 && kill $PID | /dev/null

