#!/bin/bash
chmod 755 midicsv-1.1/midicsv

for f in midi_files/*.mid 
do 
	NEWNAME=$(basename $f)
	NEWNAME="$NEWNAME.csv"
	midicsv-1.1/midicsv $f midi_csv_files/$NEWNAME
done 

python midi_csv_to_txt.py
