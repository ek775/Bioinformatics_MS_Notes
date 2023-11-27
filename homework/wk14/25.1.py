# 25.1
"""Write a python program using SQLObject to find the taxonomic lineage of a user-supplied organism name.
"""


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

# define function to get parents
def get_parents(child_id):
    """Uses list-like of name table IDs to find parent IDs."""
    child = list(Taxonomy.select(Taxonomy.q.id==child_id))
    parent_id = child[0].parentID
    #print(parent_id)
    parent = list(Taxonomy.select(Taxonomy.q.id==parent_id))
    #print(parent[0])
    is_root = False
    if parent[0].parentID != 1:
        pass
    else:
        is_root = True
    
    return parent_id, parent, is_root
    
# find taxonomic id based on generic name(s)
name_search = Name.select(
                OR(Name.q.name == f"{generic_name}",
                    LIKE(Name.q.name, f"%{generic_name}%")))
gen_names = list(name_search)

##### MAIN #####
results = {}
origin_ids = None
for n in gen_names:
    taxa_id = n.taxonomyID
    taxa_search = Taxonomy.select(Taxonomy.q.id==taxa_id)
    # record starting results as origin
    results["origin"] = list(taxa_search)
    # get parents
    origin_ids = [o.parentID for o in list(taxa_search)]

for id in origin_ids:
    i, j, root = get_parents(id)
    degree = 0
    while root == False:
        degree +=1
        # check infinite loop
        if degree == 100:
            print("infinite loop")
            exit(1)
        #continue
        i, j, root = get_parents(i)
        #print(i, j, root)
        results[f"{id}{degree}_root={root}"] = j
            

# return results to terminal
print(results)