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
    if state in endstates: # check if first state is an endstate
        LM += ['e'] # empty string accepted
        return LM
    path += [state] # add state to path
    for vert, nextState in dfa[state].items():
        # print(nextState, vert, endstates)
        if nextState not in path:
            if nextState in endstates:
                LM += vert # add path if checks pass
                path = dfsRecurse(dfa, nextState, path, LM, endstates) # recursive step
            else:
                path = dfsRecurse(dfa, nextState, path, LM, endstates) # recursive step
    return LM

def checkIfEmpty(dfa1, findP=[]):
    path, LM = [], []
    findP = dfsRecurse(dfa1['dfaSTF'], dfa1['startS'], path, LM, dfa1['endStates'])
    if findP == []:
        return 'Language empty'
    elif findP == ['e']:
        return 'e'
    else:
        for endS in findP:
                if endS not in dfa1['AlphbetSpec']: # dfs returns states it lands on, thus remove them
                    iX = findP.index(endS)
                    del findP[iX:] # removes unecessary string parts
        accL = ''.join([str(elem) for elem in findP]) # convets list to string
        return accL
if __name__ == "__main__":

    dfa1 ={}
    file1 = sys.argv[1]
    dfa1 = encodingsDFA(file1)
    # rencode(dfa1)
    checker1 = checkIfEmpty(dfa1)
    if checker1 == []:
        print('Language empty')
    else:
        print('Langauge non-empty - "'+ checker1 +'" accepted')
