import sys
import os
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO

if len (sys.argv) != 4:
    print("Invalid params: 1) In file path - 2) Out file path 3) Type ( --prot or --nuc )")
    sys.exit(1)

fasta_string = open(sys.argv[1]).read()

if sys.argv[3] == "--prot":
	result_handle = NCBIWWW.qblast("blastp", "swissprot", fasta_string)
elif sys.argv[3] == "--nuc":
	result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
else:
	print("Invalid type for blast")
	sys.exit(1)

blast_records = NCBIXML.parse(result_handle)

if os.path.exists(sys.argv[2]):
  os.remove(sys.argv[2])

E_VALUE_THRESH = 0.04

for blast_record in blast_records:
	for alignment in blast_record.alignments:
	     for hsp in alignment.hsps:
	         if hsp.expect < E_VALUE_THRESH:
	            with open(sys.argv[2], "a") as f:
		            print("****Blast Result****", file=f)
		            print("sequence:", alignment.title, file = f)
		            print("length:", alignment.length, file = f)
		            print("e value:", hsp.expect, file = f)
		            print(hsp.query[0:75] + "...", file = f)
		            print(hsp.match[0:75] + "...", file = f)
		            print(hsp.sbjct[0:75] + "...", file = f)