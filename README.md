# gbk-nt_query

Turns a gbk and fasta file into a query-able database

Simply determine your position of interest and the program will tell you the gene, amino acid and codon.

## Usage

Run the input.py as
```
python input.py [position]
```
[position] being the nucleotide position you are interested in finding out about.

This script is currently designed for the SARS-CoV-2 Reference Genome (NC_045512.2) and Human Herpesvirus 5 Cytomegalovirus (NC_006273.2)

It should theoretically work for any closed genome with a fully annotated genbank file (annotated with PGAP/Snippy is recommended)

Cool beanies.
