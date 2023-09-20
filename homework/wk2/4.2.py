# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:05:25 2023

@author: ninja
"""

#4.1
#Write a Python program to determine whether or not a DNA sequence consists of a (integer) number of (perfect) "tandem" repeats.
#Test it on sequences:
t1 = "AAAAAAAAAAAAAAAA"
t2 = "CACACACACACACAC"
t3 = "ATTCGATTCGATTCG"
t4 = "GTAGTAGTAGTAGTA"
t5 = "TCAGTCACTCACTCAG"
#Hint: Is the sequence the same as many (how many?) repetitions of its first character? 
#Hint: Is the sequence the same as many (how many?) repetitions of its first two characters?

##############################################################################
#IGNORE THIS FUNCTION - leaving here for documentation purposes of my first 
#approach to this problem.

#This function attempts to address the possibility of a tandem repeat series 
#being found mid-sequence (i.e. in the introns of a gene)
##############################################################################
def repeat_tf(input_sequence, max_repeat_dist = 6):
    pass
    """
    Tests a given sequence for repeating bases.

    Parameters
    ----------
    input_sequence : TYPE
        DESCRIPTION.
    max_repeat_dist : TYPE, optional
        DESCRIPTION. The default is 6.

    Returns
    -------
    repeat_present : TYPE
        DESCRIPTION.
    window : TYPE
        DESCRIPTION.

    """
    #handle case
    input_sequence = input_sequence.lower()
    
    #initialize key variables
    window = None
    repeat_present = False
    
    #main loop
    for p,b in enumerate(input_sequence):
        #prevent end of string indexing errors
        #compares current index/search window to max index of given seq
        if (p+2*max_repeat_dist) > (len(input_sequence)-1):
            break
        #nested loop checking for bases repeating on a cycle
        for i in range(max_repeat_dist):
            #prevent end of string indexing errors
            #compares current index/search window to max index of given seq
            #if (p+2*i) > (len(input_sequence)-1):
                #break 
            #search for repeats
            if b[p+i]==b:
                if b[p+2*i]==b:
                    window = i
                    repeat_present = True
                else:
                    continue
            else:
                continue
            
    return repeat_present, window

##############################################################################
#Last error was string indexing error due to search window running past end of 
#query string
##############################################################################


def repeat(query, max_tandem_length = 6):
    """
    Identifies tandem repeats in a given sequence by searching for a repeating 
    section of the first bases in the sequence.

    Parameters
    ----------
    query : str
        DNA sequence to be searched for tandem repeats.
    max_tandem_length : str, optional
        Maximum expected length of tandem repeats in the given sequence. 
        The default is 6.

    Returns
    -------
    repeat_present : t/f
        Indicates whether a repeat is present in the given sequence. 
        True indicates that the sequence contains a tandem repeat.
    repeat_substring : str
        Sequence of the tandem repeat, if a repeat is identified. Empty string
        is returned if no repeat is identified.
    no_of_repeats : int
        Number of sequential repeats found in a given sequence.
    perfect_repeat : t/f
        Indicates if the entire sequence is a perfect tandem repeat.
        True indicates that the tandem repeat continues and aligns with the 
        whole query sequence. 

    """
    
    #key variables
    repeat_substring = ""
    repeat_present = False
    no_of_repeats = 0
    perfect_repeat = False
    
    #main search loop
    #compares a substring of the query sequence against the whole
    #note that tandem repeat >= 2 bases
    for i in range(2, max_tandem_length):
        
        #stop at shortest repeat
        if repeat_present == True:
            break
        
        #creates substring to search for based on first bases in seq
        search_substring = query[0:i]
        #test for repeat
        if query[i:i*2] == search_substring:
            repeat_present = True
            repeat_substring = search_substring
            no_of_repeats = 1
            #count repeat length
            for n in range(len(search_substring),     #starting position
                           len(query),                  #max_range
                           len(repeat_substring)):      #step size
                if query[n:n+len(search_substring)] == search_substring:
                    no_of_repeats += 1
                #end counting once repetition stops
                else:
                    break
                
        #check for alignment/perfect repeat        
        if no_of_repeats*len(repeat_substring) == len(query):
            perfect_repeat = True
        
        #if no repeat, try longer sequence up to max_tandem_length
        else:
            continue
    
    #function output
    return repeat_present, repeat_substring, no_of_repeats, perfect_repeat
                    
    
###terminal output from final testing:

"""runcell(0, 'C:/Users/ninja/Documents/ms_bioinformatics/python_intro/homework/wk2/4.2.py')

repeat(t1)
Out[35]: (True, 'AA', 8, True)

repeat(t2)
Out[36]: (True, 'CA', 7, False)

repeat(t3)
Out[37]: (True, 'ATTCG', 3, True)

repeat(t4)
Out[38]: (True, 'GTA', 5, True)

repeat(t5)
Out[39]: (False, '', 0, False)"""    
    
    
    
    
    
    
    
    
    
    
    
    

