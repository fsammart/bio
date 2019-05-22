import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import regex as re


if len(sys.argv) != 3:
	print("Invalid params: 1) In file path 2) Out file path")
	sys.exit(1)

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]

record = SeqIO.read(in_file_name, "gb")
record_str = str(record.seq)

startP = re.compile('ATG')
nuc = record_str.replace('\n','')
rec = Seq(nuc)
longest = (0,)
for m in startP.finditer(nuc, overlapped=True):
    if len(rec[m.start():].translate(to_stop=True)) > longest[0]:
        pro = rec[m.start():].translate(to_stop=True)
        longest = (len(pro), 
                   m.start(), 
                   str(pro),
                   nuc[m.start():m.start()+len(pro)*3+3])

protein_record = SeqRecord(Seq(longest[2], IUPAC.protein), id=record.id, description= record.description + " protein translation")

with open(out_file_name, "w") as output_handle:
    SeqIO.write(protein_record, output_handle, "fasta")