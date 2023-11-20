METHODS:
************************************************************************************************
I chose to perform this exercise using two queries. The first searches for a genbank common name matching what was passed to it, and the second searches the taxonomy table for scientific names matching the possible taxonomy ids. This is accomplished by using sqlite3 to query the database and pandas to manage the information received.

DISCUSSION:
************************************************************************************************
This CLI-based tool is incredibly brittle and needs an exact match to a genbank common id. Per the instructions of this assignment, this essentially meets the MVP requirements, but it is worth noting that with most users being familiar with much more sophisticated search alogirthms from other web services and software there would likely be complaints over something this bare bones.