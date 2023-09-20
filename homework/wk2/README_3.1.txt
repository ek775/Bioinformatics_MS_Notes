Methods:

*copied and pasted the gene sequence from the course webpage into the provided code, as 
no methods have been shown in the course thus far for importing data directly from files.

(1) Wrote a short conditional statement to determine if the first 3 codons in the SASP gene
	matched the methionine codon. Result was printed to the terminal.
(2) Determined the location of the first methionine codon using the string method "find",
	and then used the modulus operator to determine the translation frame position. 
	Result was printed to the terminal using a formatted string.
(3) Used the len function in python to determine the number of nucleotides in the SASP gene.
	Result was printed to the terminal using a formatted string.
(4) Used the len function and integer division to determine the number of amino acids in the 
	SASP protein. Result was printed to the terminal using a formatted string.
(5) To calculate the GC richness, one needs to count the number of G's and C's in the SASP
	gene and then divide it into the length of the whole string. To accomplish this task
	in the cleanest code possible, I provided a function called "count" with associated
	documentation. The function was then called twice to count the number of G's and C's
	in the given sequence.  

Discussion:

(1) The first question required a fairly simple use of boolean operators, an if-else statement, and some review from coding skills introduced in lecture 1. Depending on the context in which this info is being used, it is unnecessary to utilize if-else logic and print the output to the terminal. This could easily be done in an exploratory fashion in an interactive terminal or jupyter notebook by simply evaluating the boolean statement alone.
(2) The math for this problem is fairly straightforward, but also has a similar inefficiency as problem one - for exploratory analysis the print statement may be unnecessary clutter.
(3) This problem only required the use of a built in python function to obtain the length of the sequence. Again, depending on what this info is being used for the print function may be superfluous. 
(4) I must admit I have some interpretive misgivings about this question. In context, it appears that this exercise is designed to utilize integer division along with the answer from the preceding question to determine the number of residues in the gene. However, the way the question is phrased suggests the need to determine what codons are actually translated. This requires, at a minimum, the identification of the start codon index position and the next stop codon downstream, which, can be one of 3 possible codons. The most efficient answer to this question relies on the use of regular expressions, which, we have not covered up to this point. My script answers this questions in both of its interpretations, however, I should point out that the number of loops and independent functions necessary to complete this task result in a very complicated control flow that is difficult to communicate to others - in addition to being generally tedious. It is also worth noting that this approach only works for prokaryotes, which, do not splice their exons to synthesize their proteins. 
(5) The greatest inefficiency in this solution is that it does not take advantage of the built in python string method for counting substrings. 