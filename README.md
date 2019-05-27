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

NOTA: Para correr en modo local, se debera bajar la base de datos de Swissprot a traves del siguiente link:
https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download

Descomprimir en el mismo directorio src/ del ejercicio y luego ejecutar:
```
 makeblastdb -in swissprot -dbtype prot
 ```

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

El comando anterior realiza un alineamiento multiple de las secuencias que se encuentren en archivo.fasta y deja el resultado en alignment.out







