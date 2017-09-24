#!/bin/bash

# Your task is to use for loops to display only odd natural numbers from to 1 to 99

for i in $(seq 1 100);
do
    if [[ $(($i%2)) == 1 ]]; then
	echo $i
    fi
done
	 



