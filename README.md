# Introducción a la bioinformática

## Ejercicio 1 – PROCESAMIENTO DE SECUENCIAS.

Escribir un script que lea una o más secuencias (de nucleótidos) de un archivo que contenga la información en formato GenBank de un mRNA de su gen (o genes) de interés, las traduzca a sus secuencias de amino ácidos posibles (tener en cuenta los Reading Frames) y escriba los resultados en un archivo en formato FASTA. Ustedes deben generarse su archivo GenBank de secuencias input, por ejemplo realizando una consulta de los mRNA del gen INS (que está asociado a la Diabetes) en la base de datos de NCBI-Gene y obtener uno o más resultados en formato
GenBank en un archivo de texto. Si no desean seguir trabajando con las seis secuencias de aa posibles, pueden utilizar alguna función o programa que les permita saber cual el es marco de lectura correcto y seguir con esa secuencia.
NOTA: Ver aclaración de este ejercicio al final del documento.
- Input: Archivo de secuencias Genbank (ej. NMxxxx.gbk con una o más secuencias).
- Output: Archivo de secuencias Fasta de cada ORF (ej. Xxxxx.fas con una o más secuencias de
aminoácidos).

## Ejercicio 2.a - BLAST. 

Escribir un script que realice un BLAST de una o varias secuencias (si son varias se realiza un Blast por cada secuencia input) y escriba el resultado (blast output) en un archivo. 
Nota: Pueden ejecutar BLAST de manera remota o bien localmente (si hacen ambos tienen más puntos!),
para esto deben instalarse BLAST localmente del FTP del NCBI, luego bajarse la base de datos ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/swissprot.gz y descomprimirla en un dir por ej. ncbi-blast-2.9.0+/data/, luego usar el comando ncbi-blast-2.9.0+/bin/makeblastdb sobre el archivo swissprot (el original ya está en formato FASTA) para darle formato de BLAST DB. Dependiendo de la versión de Blast suite que tengan instalado puede que en vez de makeblastdb deban utilizar el comando formatdb.
- Input: Secuencia Fasta (ej. Xxxx.fas con una o más secuencias de aminoácidos obtenidas en Ej.1).
- Output: Reporte Blast (ej. blast.out, si deciden hacer múltiples pueden generar un único o varios
archivos).

## Ejercicio 2.b – Interpretación del resultado del Blast. 

Dar una explicación del resultado Blast obtenido en términos de las secuencias encontradas y dar una explicación sobre que significan los valores estadísticos asociados a las secuencias encontradas (el capítulo 4 del libro de David Mount puede ayudarlos).

## Ejercicio 3 – Multiple Sequence Alignment (MSA).

Descargar las secuencias (en formato fasta) de 3 o más organismos distintos (otras especies) que hayan salido en los resultados del Blast. Generar un archivo multifasta con estas secuencias más su secuencia query y realizar un alineamiento múltiple con la secuencia de consulta más estas otras encontradas. Si no pueden hacerlo localmente pueden utilizar algún programa de MSA online. Intenten realizar una interpretación del resultado del alineamiento múltiple. Entregar información del MSA (el capítulo 5 del libro de David Mount puede ayudarlos).
