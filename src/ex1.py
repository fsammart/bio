import sys
import os
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

if os.path.exists(sys.argv[2]):
  os.remove(sys.argv[2])

records = SeqIO.parse(in_file_name, "gb")

for record in records:
	record_str = str(record.seq)
	rev_record_str = str(record.seq.reverse_complement())
	startP = re.compile('ATG')
	nuc = record_str.replace('\n','')
	rev_nuc = rev_record_str.replace('\n','')
	longest = (0,)
	for seq in nuc, rev_nuc:
		for m in startP.finditer(seq, overlapped=True):
			rec = Seq(seq)
			print(rec[m.start():].translate(to_stop=True))
			if len(rec[m.start():].translate(to_stop=True)) > longest[0]:
				pro = rec[m.start():].translate(to_stop=True)
				longest = (len(pro),str(pro))

	protein_record = SeqRecord(Seq(longest[1], IUPAC.protein), id=record.id, description= record.description + " protein translation")

	with open(out_file_name, "a") as output_handle:
		SeqIO.write(protein_record, output_handle, "fasta")