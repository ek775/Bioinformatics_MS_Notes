# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:49:19 2023

@author: ninja
"""

For the first problem, the string was tokenized and then 
concatenated in reverse order using slices and basic operators. 
A separate function call returns a print statement of the modified 
string.Note that this approach is tedious and not scalable for longer
strings.

The second problem uses .find() method to locate first start codon, then
returns the translation frame and start position relative to the 
whole sequence. This approach is relatively efficient, however, for 
ease of documentation/readability it would be better to define this as
its own function.