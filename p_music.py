#@author berwin xie
#@edited 6.24.14

#takes a sequence of integers (music values), puts its following note into dictionary, and use that
# to create initial matrix for markov chaining
    
#possible midi notes range from 21 to 108

import sys
import random as rand
import numpy as np

from simpleOSC import initOSCClient, sendOSCMsg
import time

#osc init
ip = "127.0.0.1"
port = 9002

initOSCClient(ip, port)

sendOSCMsg("/vol", [0.05])
sendOSCMsg("/bypass", [0])
sendOSCMsg("/roomsize", [0.0])


#CONSTANTS
#low_bound has to be one less than the lowest value
#high bound has to be one more than the highest value
low_bound = 20
high_bound = 109

#nums are the midi notes from the file (we have extracted them into an array in the main function)
def create_dict(nums): 
    dict = {}
    #for num in range(21, 109):
    for num in range(low_bound, high_bound):
        dict[num] = []
    for num in range(0, len(nums)-2):
        dict[int(nums[num])].append(int(nums[int(num)+1]))
    return dict 
    
def create_matrix(dict):
    #bad implementation: adds extra column and then deletes it. oh well
    #a = np.array([[0,0,0,0,0]])
    result = []
    for i in range(0, high_bound - low_bound - 1):
        result.append(0.)
    a = np.array([result])
    for dict_entry in range(low_bound, high_bound - 1):
        temp = []
        #instantiate the column with 0's
        for num in range(0, high_bound - low_bound - 1):
            temp.append(0.)
        dict_entry = dict_entry + 1
        nums = dict.get(dict_entry)
        #print 'what comes after ' + str(dict_entry)
        for i in nums:
            temp[i-low_bound-1] = temp[i-low_bound-1] + 1

        #usese numpy to find sum and get probability
        b = np.array([temp])
        sum = b.sum()

        #catches when there's never a connection
        if sum != 0:
            b = b/sum;
        else:
            b = b/999999

        
        #b = np.array(temp)
        a = np.dstack((a, b))
            
    a = np.delete(a[0], 0, 1)
    return a


def pick_next(matrix, query):
    column = query - low_bound - 1
    #print column
    p = rand.random()
    #print matrix
    #print query
    probability = matrix[:,column]

    #print probability
    #print probability.sum()
    cum_prob = 0.0
    count = 0
    #will add to prob until reaches 1 or p is <= the cum_prob
    for prob in probability:
        count = count + 1 
        cum_prob = cum_prob + prob
        if p <= cum_prob and prob != 0:
            return low_bound + count


    return low_bound + 1 

def midi_to_freq(midi_num):
    a = 440.0 #440 tuning
    freq = (a / 32.0) * (2.0**((midi_num - 9.0) / 12.0))
    return freq

def main(filename):
    file = open(filename, 'r')
    nums = file.readline()
    nums = nums.split(' ')
    #print nums
    dictionary = create_dict(nums) 
    init_matrix = create_matrix(dictionary)

    #this is for single matrix
    temp = pick_next(init_matrix, int(nums[0]))
    while(1):
        #4 beat measures
        for i in range(1, 5):
            #temp_matrix = init_matrix**(i%4)
            temp_matrix = init_matrix
            #print init_matrix
            temp = pick_next(temp_matrix, temp)
            time.sleep(1.0)
            
            midi_temp = midi_to_freq(temp)
            print temp
            print midi_temp
            sendOSCMsg("/freq", [midi_temp])
            sendOSCMsg("/bang", [1])




if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print 'run with one argument: text file with note values'
