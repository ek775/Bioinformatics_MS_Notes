METHODS
#####################################################################################

I started with an iterative design process based on the reverse complement generation method used in exercise 7.1 as the first approach. 

My second method alters the first approach by using a dictionary to map the bases of the original strand to the complementary bases of the computed strand. This replaces the use of the "find" method in the preceding approach.

The 3rd method in this program retains the use of the dictionary from the 2nd method, however, it radically shifts the approach to computing the complement and reversal steps by attempting to maximize the in-built functionality of python. Each step is done as a list comprehension, carrying speed advantages as well as reducing the amount of code. The map function with a lambda is able to quickly convert each base to its complement, which is then passed to the reversal iterator in the next list comprehension to generate the final sequence of bases. The bases in this final list are then concatenated back into a single string and returned as a new string.

The 4th method I used returns to the second method using a dictionary with an explicit loop structure, but it utilizes the enumerate function to do the reverse indexing for the reversal, which, saves a line of code.

DISCUSSION
#####################################################################################

The first method is by far the slowest of the methods I have shown in this program. Using python's "%timeit" magic command in an ipython terminal, I was able to time each of the functions in my program after initially assessing their basic functionality. It appears that this is largely due to the extra conditional statement and use of the .find() method. Simply replacing .find() with the use of a dictionary results in about a 30% time reduction. A similar iterative change in method 4, which, improves the readability of the code and calls fewer functions, however, does not result in nearly the same speed improvement.

The fastest computational method of the above items is in my 3rd iteration, which, completes the given task in less than half the time of the baseline method. This speed advantage comes at a slight cost, however. The map iterator is currently faster in part because because it does not contain the conditional check for non-standard bases in all of the other approaches. It is possible to use the lambda or the list comprehension methods with conditionals, however, my intent with this step was to maximize speed to see how much of a speed improvement could be gained - and at what cost. It is likely worth seeing how fast the function would execute with the conditional re-introduced.
