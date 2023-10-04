METHODS
######################################################################

This script accepts species proteome sequence files and uses biopython to determine the frequencies of the essential amino acids within them. Any number of files, compressed or extracted, may be passed in as shown here:

"python 12.1.py [file 1] [file 2] ... [file N]"

If a single file is given, the script will return the frequencies of the amino acids within that proteome, as well as the most/least common amino acids in that proteome. 

If multiple files are given, the script will return a dictionary containing the amino acid frequencies of each file passed to it, along with a separate dictionary containing the maximum, minimum, and average frequencies for each amino acid. 

Fundamentally, this script reads in the files according to its given file extension by first parsing the file name to identify the extension, and then proceeding to read the file using the appropriate biopython parser. To reduce memory usage, only the sequences themselves are actually read into further data types, which, are then used to calculate frequencies with Biopython's ProteinAnalysis object, and iteratively returned to the terminal using the above formatting and statistical analysis per the exercise instructions.

DISCUSSION
######################################################################

Completing this exercise in this manner without the use of OOP results in some nasty nested loop structures for accessing data that lead to a few bugs during scripting as well as a known issue that I commented on in the source code documentation. However, I wrote the script to be flexible with the number of files and to handle appropriate parsing of the files given to it, thus making it more reusable than a simpler script would have been, and reducing the number of command line arguments necessary to run this script. 

OOP would severely reduce the complexity of this script by allowing the creation of proper dataframe objects with associated methods for calling attributes (kinda like pandas...) instead of nested loops with buggy implementation. I would also argue that being able to dump these statistics into a machine-readable persistent file type would allow for this information to be exported to a more useful interface with a cleaner visual representation.
