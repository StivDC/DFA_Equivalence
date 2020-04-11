# (5)
# Write a program that takes two .txt file encodings of any two DFAs M and
# M′ as arguments, and prints to the screen either “equivalent” or “not equivalent”.
# Thomas Davies-Cortes 1822356

from encoding import encodingsDFA
import sys
from Symmetric import gUnion
from Emptyness import checkIfEmpty
from Reencoding import rencode

# find symmetric difference
# check if it's empty

dfa1={}
dfa2={}

file1 = sys.argv[1]
dfa1 = encodingsDFA(file1)
file1 = sys.argv[2]
dfa2 = encodingsDFA(file1)

def symmDiff(dfa1, dfa2):
    return gUnion(dfa1, dfa2) # I was too lazy to rename union, as it
    # has been coded to get the union initially, but then updated to incorporate
    # the intersections when called elsewhere.

g3 = symmDiff(dfa1, dfa2)

g3 = checkIfEmpty(g3)
# print(g3)
if g3 == 'Language empty' or g3 == '':
    print('Equivalent')
else:
    print('Not equivalent')
