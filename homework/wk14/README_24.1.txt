METHODS
************************************************************************************************
Starting from a generic organism name, 24.1 executes from the command line, queries the small_taxa.db3 database, and retrieves the matching taxonomy information for that queried species. The taxonomy ID is then used to find the appropriate scientific name for the queried organism.

DISCUSSION
************************************************************************************************
Object relational mappers are quite frankly obnoxious for a task as simple as querying a database - and this is apparent from the lack of documentation on how to query the master table or explore the database without prior knowledge in sqlobject. This exercise would be much better performed with actual SQL queries written programatically in terms of speed of execution as well as development time in my opinion. 