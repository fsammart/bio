import sys
import os
if len (sys.argv) != 3:
    print("Invalid params: 1) In file path - 2) Out file path")
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
        print "Unexpected error:", sys.exc_info()[0]
        raise

getmotifs(open(sys.argv[1]))
