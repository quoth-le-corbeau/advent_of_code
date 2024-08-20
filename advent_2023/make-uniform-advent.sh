#!/bin/bash

for dir in */; do
	echo "scanning directories in" */
	if [ -d "$dir" ]; then
		echo "$dir"
		ls "$dir"
		if [ -f "$dir/1.py" ]; then
			mv "$dir/1.py" "$dir/p1.py"
		fi
		
		if [ -f "$dir/2.py" ]; then
			mv "$dir/2.py" "$dir/p2.py"
		fi

		touch "${dir}eg.txt"
		touch "${dir}input.txt"
	fi
done
