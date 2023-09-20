Methods:

A function was defined that would identify tandem repeats in a given query string of DNA by doing the following:
	1) iteratively attempt to match slices of the first n-bases in the query string with 	successive slices of n-bases in order to identify presence of a tandem repeat.
	2) count the number of repeats to identify the length of the tandem repeat
	3) identify whether the repeat is a perfect repeat or contains misalignments/errors

A proper docstring and notes were provided for this function as well as the terminal output from the final test on the given test sequences in the source code. See documentation for further details.

################################################################################################
Discussion:

This is a fairly complicated task that solves a practical problem in bioinformatics studies. My approach, while relatively effective for given excercise, is built upon a few key assumptions that are unlikely to hold true in different contexts. 

(1) This function assumes that the tandem repeat starts at the very first base in the sequence. For the given test strings, this is mostly true, however, for this function to be practical in searching a genome for tandem repeats it would have to be wrapped in a separate function that identifies repetitive sequences and passes them to my function at the first repeat. 

(2) This function assumes that the tandem repeats will repeat perfectly at least once before imperfections occur. In a context where we are searching a whole genome, this assumption may serve to filter out short repeats that occur due to random chance with little practical value. However, as we can see in test sequence 5, my function tells us there is no repeat here while we can arguably see the sequence repeat with a SNP variation in the 4th position, or, repeat mid-sequence. 

It is also worth discussing the inefficiencies in how much code was written to accomplish some basic string matching comparisons, as well as the ways that the above assumptions could be addressed using regular expressions. Python contains a module called "re" which provides the necessary regex tools for many string operations and string comparison operations. Using regex, "fuzzy matching" can address the 2nd assumption in my program, and having additionl built-in string modification/comparison operators eliminates many of the nested loops that were necessary to accomplish basic search functionality within the query string.

The biggest advantage of regex, however, is the ability to address the first assumption. Looping with regex allows us to search for general patterns in a given query, rather than the explicit search string that I generated within my function, thus enabling a more general search for ANY tandem repeat pattern instead of a procedurally generated set of explicit strings to check for.