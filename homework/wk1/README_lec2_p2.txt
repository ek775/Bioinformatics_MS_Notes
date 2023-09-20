The solution to the second problem uses the .find() method to locate the first start codon, then
returns the translation frame and start position relative to the 
whole sequence. This approach is relatively efficient, however, for 
ease of documentation/readability it would be better to define this as
its own function.