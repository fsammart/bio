import sys
import os
from Bio import SeqIO
if len (sys.argv) != 5:
    print("Invalid params: 1) In file path - 2) Out file for domain analysis 3) Nucleotide gbk 4) Out file for ORF" )
    sys.exit(1)

def getmotifs(file_content):
    try:
        print("Ejecutando EMBOSS prosextract")
        f = open('temp_fasta.fasta', 'w')
        f.write(file_content.read())
        f.close()
        os.system('prosextract -prositedir prosite')
        print("prosextract finalizado")
        print("Analizando motifs")
        os.system("patmatmotifs temp_fasta.fasta " + sys.argv[2])
        os.remove('temp_fasta.fasta')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def getorf():
    SeqIO.convert(sys.argv[3], "genbank", "temp.fasta", "fasta")
    os.system("getorf temp.fasta " + sys.argv[4])
    os.remove("temp.fasta")


getmotifs(open(sys.argv[1]))
getorf()
