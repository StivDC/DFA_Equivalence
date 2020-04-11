
def rencode(dfa):

    print(dfa['NumbOfStates'])
    print(' '.join(str(key) for key in dfa['dfaSTF'].keys()))
    print(dfa['sizeOfAlpha'])
    print(*dfa['AlphbetSpec'])
    for v in dfa['dfaSTF'].values():
        dummyL=[] # used so that list can be spliced and printed without a trailing space
        for k in v.values():
            dummyL.append(k)
        print(*dummyL) # splices list and prints
    print(dfa['startS'])
    print(dfa['nOfendStates'])
    print(*dfa['endStates'])
