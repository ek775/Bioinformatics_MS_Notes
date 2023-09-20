Methods:
************************************************************************************************
defined a reverse-complement function that accomplishes the requested task by looping through the sequence in reverse and concatenating the complementary base to a new string. The rest of the script essentially just prints the output by listing out the primers we wish to compute the reverse-complement for and then iteratively calling the function to print each of the listed primers.

Discussion:
************************************************************************************************
This function was based heavily on previous code used to accomplish the same task with some iterative improvements such as the use of the .find() method to identify the complementary base. The main improvement that could be made at this point is simply to place this function in a script or library that could be recalled instead of frequent copying and pasting of code. 