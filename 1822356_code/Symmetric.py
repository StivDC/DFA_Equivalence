# (3)
# Write a program that takes two .txt file encodings of any two DFAs M and M′
# as arguments, and prints to the screen the encoding of a DFA that recognises
# the symmetric difference of L(M) and L(M′).

# get complement of d1, intersect, d2 = d3
# get complemeent of d2 intersect d1 = d4
# unnion d3, d4
# Thomas Davies-Cortes 1822356

import copy
import sys
from encoding import encodingsDFA
from Complementation import Complement
from Intersection import gIntersect
from Reencoding import rencode

def gd3(d1, d2):
    d1 = Complement(d1) # get complement first then intersect
    return gIntersect(d1, d2)

def gd4(d1, d2):
    d2 = Complement(d2) # get complement first then intersect
    return gIntersect(d1, d2)

def gUnion(dfa1, dfa2):
    # d3 =dfa1
    # d4 =dfa2
    dfa3 = copy.deepcopy(dfa1) # deep copy of dictionary so that the pointers don't get messed up
    dfa4 = copy.deepcopy(dfa2)

    d3 = gd3(dfa1, dfa2) # get complement dfa1 intersect dfa2
    d4 = gd4(dfa3, dfa4) # get complement dfa2 intersect dfa1

    dfaL1 = d3['dfaSTF'] # gets the states with transition functions for ease of access
    dfaL2 = d4['dfaSTF']

    dfa3={}

    for d1K, d1V in dfaL1.items():
        adK = list(d1V) # creates a list of alphabet values from the transition state
        for d2K, d2V in dfaL2.items():
            stD={} # creates a new dictionary to combine DFA1 and DFA2
            for (D1VK, D1VV), (D2VK, D2VV) in zip(d1V.items(), d2V.items()):
                stD[D2VK]=str(D1VV)+str(D2VV) # updates dictionary with new state and transition functions
            dfa3[(str(d1K)+str(d2K))] = stD # gives states for DFA language


    numOfStates = len(dfa3)
    sizeOfAlpha = dfa1['sizeOfAlpha']
    alphabetK = dfa1['AlphbetSpec']
    startS = next(iter(dfa3)) # Gets first state in dictionary
    # Treat each accept state separately
    endStates = []
    # print(d3['endStates'])
    # print(d4['endStates'])
    for states in dfa3.keys():
        # print(states)
        if (states[:int(len(states)/2)] in d3['endStates']) or (states[int(len(states)/2):] in d4['endStates']):
                    # checks first half of state and checks whether it is in the first DFA's end states,
                    # then does same for second half with second DFA's end states and then if either are within their corresponding end
                    # states it will add them to the new endstates list
            endStates.append(states[:int(len(states)/2)] + states[int(len(states)/2):])

    nOfendStates = len(endStates)
    return {'NumbOfStates': numOfStates,
     'dfaSTF': dfa3, 'sizeOfAlpha': sizeOfAlpha, 'AlphbetSpec': alphabetK,'startS': startS,
      'nOfendStates': nOfendStates, 'endStates': endStates}



if __name__ == "__main__":

    dfa1 ={}
    dfa2={}

    file1 = sys.argv[1]
    dfa1 = encodingsDFA(file1)
    file1 = sys.argv[2]
    dfa2 = encodingsDFA(file1)

    dfa3 = gUnion(dfa1, dfa2)
    #
    rencode(dfa3)
