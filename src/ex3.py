import sys
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline


if len (sys.argv) != 3:
    print("Invalid params:")
    print("1) Multifasta input file")
    print("2) MSA output file")
    sys.exit(1)

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]

clustalw_cline = ClustalwCommandline("clustalo", infile=in_file_name, outfile=out_file_name)
stdout, stderr = clustalw_cline()

