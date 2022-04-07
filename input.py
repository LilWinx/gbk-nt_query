from logging import raiseExceptions
import os
import sys
import position_product
import position_nucleotide
import position_protein

"""
turns a fasta and gbk file into a command that can query any position within the genome, and tell you what the nucleotide and amino acid + codon in a query position.
to use the script, you just need to do python input.py YOUR_POSITION

dependencies
you must have biopython installed
easy install is just on powershell or terminal
pip install biopython
"""

if len(sys.argv) < 2:
    raise Exception('no input')

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, "data/NC_045512.2.fasta")
genbank = os.path.join(dirname, "data/NC_0045512.2-mod.gbk") 

product = position_product.position_product(int(sys.argv[1]), genbank, file)
nucleotide = position_nucleotide.position_nucleotide(int(sys.argv[1]), file)
protein = position_protein.position_protein(int(sys.argv[1]), genbank)

print(f"the position {sys.argv[1]} is in the {product}, the nucleotide is {nucleotide} and the amino acid is {protein}")