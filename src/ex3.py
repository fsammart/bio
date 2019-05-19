import sys
from Bio import AlignIO

if len (sys.argv) != 3:
    print("Invalid params:")
    print("1) multifasta input file")
    print("2) MSA output file")
    sys.exit(1)

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]

# Parsing multi-fasta file
alignments = list(AlignIO.parse('files/'+in_file_name, "fasta"))

for alignment in alignments:
    with open("files/"+out_file_name, "a") as f:
        print(alignment, file=f)