import re
import os
from plistlib import load
from urllib.parse import urlparse

# Function for finding the path to The Archive
#####
# Set the active archive path
def TheArchivePath():
#  Variables that ultimately revel The Archive's plist file.
    bundle_id = "de.zettelkasten.TheArchive"
    team_id = "FRMDA3XRGC"
    fileName = os.path.expanduser(
        "~/Library/Group Containers/{0}.{1}.prefs/Library/Preferences/{0}.{1}.prefs.plist".format(team_id, bundle_id))
    with open(fileName, 'rb') as fp:
        pl = load(fp) # load is a special function for use with a plist
        path = urlparse(pl['archiveURL']) # 'archiveURL' is the key that pairs with the zk path
    return (path.path) # path is the part of the path that is formatted for use as a path.
    
#  Use
    
 #####
# Variables
#####
zettelkasten = TheArchivePath()

# Set the search terms and spacing variable
search_terms = ['sky', 'tree', 'cloud']
spacing = 5

# Create a regular expression that matches all permutations of the search terms
permutations = []
for i in range(len(search_terms)):
    for j in range(i+1, len(search_terms)):
        for k in range(j+1, len(search_terms)):
            permutation = fr'\b(?:\S*?{search_terms[i]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[j]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[k]}\S*?|\S*?{search_terms[k]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[j]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[i]}\S*?|\S*?{search_terms[i]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[k]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[j]}\S*?|\S*?{search_terms[k]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[i]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[j]}\S*?|\S*?{search_terms[j]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[i]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[k]}\S*?|\S*?{search_terms[j]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[k]}\S*?\W+(?:\w+\W+){{0,{spacing}}}\S*?{search_terms[i]}\S*?)\b'
permutations.append(permutation)
regex = '|'.join(permutations)

# compile regex
# regex = re.compile(regex.format(search_terms=search_terms, spacing=str(spacing)))
# regex = re.compile(regex.format(search_terms=search_terms, spacing=str(spacing)).replace('{', '{{').replace('}', '}}'))
# regex = re.compile(regex.format(search_terms=search_terms, spacing=spacing))



# Set the directory to search
directory = '/Users/will/Dropbox/zettelkasten/'

# Search all files in the directory for the regular expression
for file in os.listdir(zettelkasten):
    if file.endswith('.md'):
        filepath = os.path.join(zettelkasten, file)
        with open(filepath, 'r') as f:
            for line in f:
                contents = f.read()
                if matches := re.findall(regex, contents, re.IGNORECASE):
                # if match := regex.search(line):
                    print(f'{file}: {matches}')