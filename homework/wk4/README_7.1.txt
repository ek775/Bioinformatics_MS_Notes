METHODS
#####################################################################################

For developing command line functionality, the program needs to be able to read the primers from the file passed to it. In this case, comments are contained in the file, delimited with a "#" symbol like in code. To remove these, I utilized a nested loop structure stripping out the comments line by line based on formatting and appending the primers to a new list.

The reverse complement was iteratively generated using the same basic structure we have been using for this task in this class and stored in several functions. Those functions were then called iteratively over the whole list of primers and printed to the terminal. 

DISCUSSION
#####################################################################################

The main goal of this assignment was essentially to add functionality to a program we have written multiple times throughout this class. Because the core of the function is essentially the same, it has the same advantages and drawbacks as previous exercises.

However, reading a file with additional formatting considerations is new to us and can be somewhat complex depending on the structure of the data. Luckily, the file we are reading from for this exercise is relatively simple and the data is stored with white space delimiters on a line by line basis with easily demarcated comments. I chose a relatively implicit approach, and skipped to the next line once the iterator ran accross a "#" symbol. This method is computationally somewhat slower than other approaches, however, it will be far more tolerant of certain errors than a slice method - which is based on location of the data and the assumption that there are 2 primers per line. 