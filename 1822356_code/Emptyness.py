# (4)
# Write a program that takes a .txt file encoding of any DFA M as an argument,
# and displays the following output behaviour:
# Thomas Davies-Cortes 1822356

from encoding import encodingsDFA
from Reencoding import rencode
import sys


def dfsRecurse(dfa, state, path, LM, endstates):
    if endstates == []: # edge case for no endstates
        LM = []
        return LM
    if state in endstates: # check if current state is an endstate
        if LM == []:
            LM+=['e']
        return LM
    path += [state] # add state to path for stack
    for vert, nextState in dfa[state].items(): # go to through neighbour states
        if nextState not in path:
            LM += vert # add
            return dfsRecurse(dfa, nextState, path, LM, endstates) # recursive step
    return [] # case for end state not found

def checkIfEmpty(dfa1, findP=[]):
    path, LM = [], []
    findP = dfsRecurse(dfa1['dfaSTF'], dfa1['startS'], path, LM, dfa1['endStates'])
    if findP == []:
        return 'Language empty'
    elif findP == ['e']:
        return 'e'
    else:
        accL = ''.join([str(elem) for elem in findP]) # converts list to string
        return accL
if __name__ == "__main__":

    dfa1 ={}
    file1 = sys.argv[1]
    dfa1 = encodingsDFA(file1)
    # rencode(dfa1) not needed
    checker1 = checkIfEmpty(dfa1)
    if checker1 == 'Language empty':
        print('Language empty')
    else:
        print('Langauge non-empty - "'+ checker1 +'" accepted')
