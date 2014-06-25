import csv
import sys

def main():
	f_in = csv.reader(open(sys.argv[1], 'r'))
	f_out = open('note_files/output.txt', 'wb') 
	for line in f_in:
		if ' Note_on_c' in line:
			f_out.write(line[4].strip() + ' ')

if __name__ == '__main__':
	main()