import re
import sys
import os
from itertools import islice
import urllib.request

BLAST_RESULT_SIZE = 11
RESULT_FILE = "patternHits.out"

if len (sys.argv) != 3:
    print("Invalid params: 1) In file path - 2) Pattern")
    sys.exit(1)

file_path = sys.argv[1];
pattern = sys.argv[2];

regex = re.compile('sp\|.*\|')

if os.path.exists(RESULT_FILE):
  os.remove(RESULT_FILE)

with open(file_path) as f:
    while True:
        next_n_lines = list(islice(f, BLAST_RESULT_SIZE))
        chunk = ''.join(next_n_lines)
        if pattern in chunk:
            with open(RESULT_FILE, "a") as out_handle:
               print(chunk, file=out_handle)
            full_accession = re.search(regex, next_n_lines[1]).group(0)
            accession = full_accession[3:9];
            content = urllib.request.urlretrieve("https://www.uniprot.org/uniprot/"+ accession + ".fasta", accession + ".fasta")
        if not next_n_lines:
            break

