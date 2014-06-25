import sys
import random as random

def main(low, high, length):
    file = open('nums.txt', 'wb')
    #random.seed([])
    for i in range(0, int(length)):
        file.write(str(random.randint(int(low), int(high))))
        file.write(' ')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print '3 arguments: low bound, high bound, number of values'
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
