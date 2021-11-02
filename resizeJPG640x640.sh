#!/bin/bash
for f in *.jpg
do
	echo "Working on file $f"
	convert $f -resize 640x640 $f
done
