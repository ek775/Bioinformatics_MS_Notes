METHODS
************************************************************************************************
Starting from a generic organism name, 25.1 executes from the command line, queries the small_taxa.db3 database, and retrieves the matching taxonomy information for that queried species. This is recorded as the "origin", from which the program procedes to search for parent organisms in the taxonomy table via parent IDs listed in each entry. The final results and their relationships are recorded in the dictionary that is printed to the terminal.

DISCUSSION
************************************************************************************************
Object relational mappers are quite frankly obnoxious for a task as simple as querying a database - and this is apparent from the lack of documentation on how to query the master table or explore the database without prior knowledge in sqlobject. This exercise would be much better performed with actual SQL queries written programatically in terms of speed of execution as well as development time in my opinion. 