"""Write a python program using SQLObject to lookup the scientific name for a user-supplied organism name."""

from sqlobject import *
import os.path
import sys

generic_name = sys.argv[1]

#specify paths, create connection, create sqlobject classes based on introspection
db = 'small_taxa.db3'
conn_str = os.path.abspath(db)
conn = 'sqlite:' + conn_str

sqlhub.processConnection = connectionForURI(conn)

class Taxonomy(SQLObject):
    class sqlmeta:
        fromDatabase = True

class Name(SQLObject):
    class sqlmeta:
        fromDatabase = True

# find taxonomic id based on generic name(s)
name_search = Name.select(
                OR(Name.q.name == f"{generic_name}",
                    LIKE(Name.q.name, f"%{generic_name}%")))
gen_names = list(name_search)
print(gen_names)

# find scientific name
results = []
for n in gen_names:
    taxa_id = n.taxonomyID
    print(taxa_id)
    taxa_search = Taxonomy.select(Taxonomy.q.id==taxa_id)
    print(taxa_search)
    for result in list(taxa_search):
        print(result)
        results.append(result.scientificName)

# return results to terminal
print(results)