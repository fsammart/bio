import sys
import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]

record = SeqIO.read('files/'+in_file_name, "gb")

protein_sequence = record.seq.translate()
protein_record = SeqRecord(protein_sequence,
                   id=record.id, name=record.name,
                   description=record.description)

SeqIO.write(protein_record, 'files/'+out_file_name, "fasta")