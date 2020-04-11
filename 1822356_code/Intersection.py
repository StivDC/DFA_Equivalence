# Get intersect (2)
# (i)  Give a state diagram for a DFA that recognises L(D1)∩L(D2) (whether
# obtained from your program in part (ii) below or not).

# (ii) Write a program that takes two .txt file encodings of any two DFAs M
# and M′ as arguments, and prints to the screen the encoding of a DFA
# that recognises L(M) ∩ L(M′).
# from encoding import encodingsDFA

# Thomas Davies-Cortes 1822356

from Reencoding import rencode
from encoding import encodingsDFA
import sys

def gIntersect(dfa1, dfa2):

    dfaL1 = dfa1['dfaSTF'] # gets the states with transition functions for ease of access
    dfaL2 = dfa2['dfaSTF'] # hence named dfa S(states) TF(Transition function)
    # print(dfa1['endStates'], 'dfa1') debug lines
    # print(dfa2['endStates'], 'dfa2')
    dfa3={} # empty dic for new states

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
    # Treat each accept state seperatly
    endStates = []
    for states in dfa3.keys():
        if (states[:int(len(states)/2)] in dfa1['endStates']) and (states[int(len(states)/2):] in dfa2['endStates']):
            # checks first half of state and checks whether it is in the first DFA's end states,
            # then does same for second half with second DFA's end states and then iff both are within their corresponding end
            # states it will add them to the new end states list
            endStates.append(states[:int(len(states)/2)] + states[int(len(states)/2):]) # concatenates and adds to new end states
            
    # endStates = [str(x) + str(y) for x in dfa1['endStates'] for y in dfa2['endStates']] First incorrect implementation
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

    dfa3 = gIntersect(dfa1, dfa2)

    rencode(dfa3)

# {'NumbOfStates': 3, 'dfaL': {'x': {'a': 'z', 'b': 'y'},
# 'y': {'a': 'z', 'b': 'z'}, 'z': {'a': 'y', 'b': 'z'}}, 'sizeOfAlpha': 2,
# 'AlphbetSpec': ['a', 'b'], 'startS': 'x', 'nOfendStates': 1, 'endStates': ['z']}
