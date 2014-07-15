import csv
import sys
import os

path = 'midi_csv_files/'
def main():	
    for filename in os.listdir(path):
        f_out = open('note_files/' + filename +  'text.txt', 'wb') 
        f_in = csv.reader(open(path + filename, 'r'))
        for line in f_in:
            if ' Note_on_c' in line:
                f_out.write(line[4].strip() + ' ')

    print os.listdir(path)
if __name__ == '__main__':
    main()
