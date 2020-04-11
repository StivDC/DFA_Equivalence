# get complementation (1)
# Write a program that takes a .txt file encoding of any DFA M as an argument,
# and prints to the screen the encoding of a DFA that recognises L(M).
# Thomas Davies-Cortes 1822356

from encoding import encodingsDFA
from Reencoding import rencode
import sys

def Complement(dfa): # makes all none accepting states accepting states and vice versa
    for state in dfa['dfaSTF']:
        if state not in dfa['endStates']:
            dfa['endStates'].append(state)
        else:
            dfa['endStates'].remove(state)
    dfa['nOfendStates'] = len(dfa['endStates']) # update number of end states
    return dfa

if __name__ == "__main__":

    file1 = sys.argv[1]
    dfa = encodingsDFA(file1)
    # print(dfa) debug line
    dfa = Complement(dfa)
    rencode(dfa)
