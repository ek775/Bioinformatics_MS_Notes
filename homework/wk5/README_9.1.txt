METHODS
##############
The general approach to this problem is broken down into the 3 subtasks given by defining them each as their own function. One function handles translation, another handles the computation of the reverse complement strand, and another handles loose 3rd base pairing - as noted in each function's documentation. 

Building upon the code written for exercise 8.2, this program can be executed from the command line by calling python on this script and passing a sequence file and ncbi codon table file to it in this format: 

#python 9.1.py [sequence_file] [codon_table]

The sequence file is expected to be a single sequence in a line-by-line file format such as a text file, and the ncbi codon table should be formatted as provided by the taxonomy resource page.

The program will use these files to translate a given amino acid sequence in each of the 3 possible translation frames according to the given codon table, and will return the results for both the given strand and its complement on the command line.

DISCUSSION
##############
Compared to the code for 8.2, this is much more efficient due to the use of more built-in python libraries/functionality and overall appears more "pythonic". This results in two primary benefits: (1) The code is cleaner and easier to read, which lends itself to ease of use and documentation, and (2) The code is more flexible and less error-prone because there is less boiler-plate code. 

The key weakness of this program in its current state is frontloaded on the file parsing tasks. Because we are not using standardized file formats, parsing has to be done manually with fairly explicit code. This leads to the issue that slight changes to input file formatting due to updates, errors, or other inconsistencies can cause this program to read the file incorrectly and cause downstream errors - whether they raise an exception or not. 