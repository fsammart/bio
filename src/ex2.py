import sys
import os
from Bio.Blast import NCBIWWW
from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast import NCBIXML
from Bio import SeqIO

E_VALUE_THRESH = 10
RESULTS_XML = "results.xml"
PROT_DB = "swissprot"
NUC_DB = "nt"


if len (sys.argv) != 5:
    print("Invalid params: 1) In file path - 2) Out file path 3) Type ( --prot or --nuc ) 4) Mode ( --online --local)")
    sys.exit(1)

fasta_string = open(sys.argv[1]).read()

if sys.argv[3] == "--prot":
	if sys.argv[4] == '--online':
		result_handle = NCBIWWW.qblast("blastp", PROT_DB, fasta_string, expect=E_VALUE_THRESH)
		with open(RESULTS_XML, "w") as out_handle:
			out_handle.write(result_handle.read())
		result_handle = open(RESULTS_XML)
	elif sys.argv[4] == '--local':
		blastx_cline = NcbiblastxCommandline(cmd='blastp', query=sys.argv[1], db=PROT_DB, evalue=E_VALUE_THRESH, out=RESULTS_XML, outfmt=5)
		stdout, stderr = blastx_cline()
		result_handle = open(RESULTS_XML)
	else:
		print("Invalid Mode for blast")
		sys.exit(1)
elif sys.argv[3] == "--nuc":
	result_handle = NCBIWWW.qblast("blastn", NUC_DB, fasta_string)
else:
	print("Invalid type for blast")
	sys.exit(1)

blast_records = NCBIXML.parse(result_handle)

if os.path.exists(sys.argv[2]):
  os.remove(sys.argv[2])

for blast_record in blast_records:
	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
			with open(sys.argv[2], "a") as f:
			   print("****Blast Result****", file=f)
			   print("sequence:", alignment.title, file = f)
			   print("length:", alignment.length, file = f)
			   print("e value:", hsp.expect, file = f)
			   print("gaps:", hsp.gaps, file = f)
			   print("identities:", hsp.identities, file = f)
			   print("positives:", hsp.positives, file = f)
			   print("score:", hsp.score, file = f)
			   print(hsp.query[0:75] + "...", file = f)
			   print(hsp.match[0:75] + "...", file = f)
			   print(hsp.sbjct[0:75] + "...", file = f)