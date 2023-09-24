METHODS
##############
CLI functional program that counts each occurence of a character in a string, in this case expected to be a single-strand DNA sequence written in a text file. This count is then used to calculate the frequency of each base in the sequence and printed to the terminal. 

DISCUSSION
##############
In all honesty, this script seems like it would be more useful as an importable functionality than as a command line program. If I were to write this script for my own usage, I would simply define a count function and a frequency function and import said functions into larger programs where they can be used to do more complex analysis. In this program's current format, the frequencies of bases in the DNA are simply printed to the terminal, which, is not useful as an input for downstream usage. 