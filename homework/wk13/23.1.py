"""
Read through an online course in SQL
sqlcourse.com, sql-tutorial.net, ...

Write a python program to lookup the scientific name for a user-supplied organism name.
"""

import sys
import sqlite3
import pandas as pd

#organism name
query = [str(sys.argv[1])]
conn = sqlite3.Connection('taxa.db3')

#find id for common name
q1 = """
    SELECT tax_id
    FROM name
    WHERE name_class = 'genbank common name' AND name = ?
    """
poss_ids = pd.read_sql(sql=q1, con=conn, params=query)

id = [int(poss_ids["tax_id"][0])]

#find scientific name
q2 = """
    SELECT *
    FROM taxonomy
    WHERE tax_id = ?
    """
sci_name = pd.read_sql(sql=q2, con=conn, params=id)

print(sci_name)