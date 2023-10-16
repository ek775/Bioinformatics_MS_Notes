---METHODS---

Using the requests library, this script pulls a single entry from the uniprotkb database at a hardcoded URL using their REST API. The data is then saved in a file and parsed with element tree so we are able to identify the references for the entry. The results from this search are then passed to a dictionary where they are saved as a CSV file and printed to the terminal in CSE citation format.

---DISCUSSION---

Attached you will find a citations.csv file, as well as the P50052.xml data and the base script itself. Because I wrote the results to a couple of files, you can easily see the results of my script at various points and troubleshoot the program based on this information. This script is pretty bare bones and does not perform data cleaning tasks or account for different xml dialects. This leads to one error that I found at the very end of my code due to some missing metadata items that were not given a null value and simply omitted from the element attributes entirely. 

In short, this script works, but it is extremely brittle and I would need to generalize much more of its pipeline before using it to do anything useful.