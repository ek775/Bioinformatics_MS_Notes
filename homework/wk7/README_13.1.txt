METHODS
################################################################################################

Essentially the only change that should have been needed from the lecture code was to persist the data read in from the file and append it to a dictionary such that it could be used to find the maximum number of reads over a given position. 

Due to the relatively primitive nature of the tools given for this assignment, "heterozygosity" was considered to exist for any reference aligned read which gave more than one base at the given position. It is not clear from the instructions or the data what the various "reads" represent, and no documentation is given for the data, thus it is impossible to determine what alleles are present, or what counts as heterozygosity in this context. 

The "quality control" code from lecture seems to result in the omission of every single data point from the data due to empty truisms being returned in the control flow logic - see pysam's documentation on pileup objects for details. Since the lecture material does not seem to indicate what the significance of each conditional is (nor where any of it should be executed in the control flow), troubleshooting this code is near impossible and use of the embedded quality control measures in the metadata, per pysam's documentation, should be considered in further analysis. 

DISCUSSION
################################################################################################

This entire assignment requires clarification, and the given scripts require more than a 2-minute afterthought explanation during a lecture which supposedly introduces the capacities of this library. Much of the given scripts needed to be amended even to get them to run with the current version of pysam.

I was able to produce a useful result prior to the "quality control" step of this exercise, however, the quality control assessments eliminate all data points and are very poorly explained leading to questions over why those data points were filtered out. According to the documentation, pysam.PileupRead objects have an attribute indel that is a numerical data type, thus leading to the checking of the attribute indel's non-None-type value always returning that it exists and omitting every single data point. Similar issues can be found in several other steps from slide 20 code, and there is no documentation to assist in debugging it short of a straight up rewrite.