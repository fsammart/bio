# Introducción a la bioinformática

## Instalación

```
python3 -m pip install --user virtualenv
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Ejecución

Primero correr:
```
source env/bin/activate
```
Luego, según el ejercicio:

# Ejercicio 1:

```
python src/ex1.py [archivo.gbk] [archivo.fasta]
```
Reemplazar [archivo.gbk] por el archivo que se quiere traducir. El resultado estará en [archivo.fasta]

Ejemplo:

```
python src/ex1.py BRCA2.gbk salida.fasta
```
El comando anterior traduce el archivo BRCA2.gbk y deja el resultado en el archivo salida.fasta

# Ejercicio 2:

```
python src/ex2.py [archivo.fasta] [archivo.out] [--prot o --nuc] [--local o --online]
```
Parametros:
--prot: indica que es una secuencia de aminoacidos y por lo tanto se realiza un blastp
--nuc: indica que la secuencia es de nucleotidos y por lo tanto se realiza un blast
--local: indica que la consulta se realiza con una base de datos swissprot local
--online: indica que la consulta se realiza online

Requisitos para correr en modo local

- Para correr en modo local, se debera bajar la base de datos de Swissprot a traves del siguiente link:
https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download

Descomprimir en el mismo directorio src/ del ejercicio y luego ejecutar:
```
 makeblastdb -in swissprot -dbtype prot
 ```
- Bajar Blast del siguiente link e instalarlo:
https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download 

Ejemplo:

```
python src/ex2.py salida.fasta blast.out --prot --online
```

El comando anterior ejecuta un blastp sobre la secuencia de aminoacidos que se encuentra en [salida.fasta] y deja el resultado en el archivo [blast.out]. El --online especifica que la consulta blast se realice online.


# Ejercicio 3:

```
python src/ex3.py [archivo.fasta] [archivo.out] 
```
Reemplazar [archivo.fasta] por el archivo con las secuencias que se quiere alinear. El resultado estará en [archivo.out]

Ejemplo:

```
python src/ex3.py archivo.fasta alignment.out
```

El comando anterior realiza un alineamiento multiple de las secuencias que se encuentren en archivo.fasta y deja el resultado en alignment.out. 

Requisitos:
 - Bajar ClustalW del siguiente link: 
 http://www.clustal.org/omega/ 
 
 Seguir los pasos para su instalación
 
 # Ejercicio 4:
 
 ```
python src/ex4.py [blast.out] pattern 
```
El comando anterior busca en el archivo blast.out, la salida del ejercicio 2, el pattern especificado. 
Para cada hit encontrado que coincide con el pattern, busca en Uniprot el archivo fasta correspondiente.

Ejemplo:

 ```
python src/ex4.py blast.out MPIGS
```
El comando anterior busca todos los hits en blast.out que contienen la secuencia de nucleotidos MPIGS

 # Ejercicio 5:
 
 ```
python src/ex5.py [protein.fasta] [domain.out] [nucleotide.gbk] [orf.out] 
```
El comando anterior realiza un analisis de los dominios de la proteina [protein.fasta]. Deja el resultado en [domain.out]. A continuacion realiza el analisis de los ORF del archivo [nucleotide.gbk] y deja el resultado en [orf.out]

Nota:
Es necesario correr el comando anterior con sudo para poder realizar correctamente el procesamiento de los archivos prosite

Requisitos:
 - Tener los archivos prosite.doc y prosite.dat dentro de un directorio llamado prosite, ubicado en el mismo directorio que el archivo ejecutable. Los archivos se pueden descargar del siguiente link:
ftp://ftp.expasy.org/databases/prosite

 # Autores:
 - Julián Palacci
 - Agustín Lavarello
 - Santiago Swinnen

 
 







