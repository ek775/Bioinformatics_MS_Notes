"""
Write a program to pick out, and print, the references of a XML format UniProt entry, in a nicely formatted way.
"""
#imports
import requests
import xml.etree.ElementTree as ET

# get data from API
# web location of type-2 angiotensin II receptor data from uniprotkb
data_URL = 'https://rest.uniprot.org/uniprotkb/P50052.xml'
query_parameters = {"downloadformat":"xml"}

# get data
print("fetching data...")

response = requests.get(data_URL, params=query_parameters)
print(response.url)
print(response.status_code)

# read xml data into element tree
if response.status_code==200:
    print("downloading file...")
    filename = data_URL.split("/")[-1]
    with open(filename, mode="wb") as file:
        file.write(response.content)
    print("---file downloaded---")
else:
    print("error fetching data")
    exit(1)

# parse file to find references and attach references to a list
print("getting references...")

ns = {"default" : "http://uniprot.org/uniprot"} # handle namespace

document = ET.parse(filename)
root = document.getroot()
references = [ref for ref in root[0].findall("default:reference", ns)]

# pick out the citation elements in each reference and append them
citations = []
for ref in references:
    cit = ref.find("default:citation", ns)
    authors = cit.find("default:authorList", ns).findall("default:person", ns)
    title = cit.find("default:title", ns)
    meta = cit.attrib
    # filter citations with missing elements
    if authors==None or title==None or meta==None:
        continue
    # reorganize the filtered data for easy access
    full_cit = {"Authors":[name.attrib["name"] for name in authors],
                "Title":title.text,
                "Info":meta}
    # append
    citations.append(full_cit)

# export as csv because I hate printing this shit out
print("saving references...")
import csv
with open("citations.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(citations[0].keys())
    writer.writerows([i.values() for i in citations])

# pretty print
print()
print("---CITATIONS---")
for c in citations:
    print(f'{c["Authors"]}.{c["Info"]["date"]}.{c["Title"]}.{c["Info"]["name"]}.{c["Info"]["volume"]}:{c["Info"]["first"]}-{c["Info"]["last"]}')
    print()

exit(0)
