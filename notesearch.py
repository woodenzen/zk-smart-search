import re
import os
from plistlib import load
from urllib.parse import urlparse
from archive_path import TheArchivePath

    
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