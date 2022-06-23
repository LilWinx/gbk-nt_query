from logging import raiseExceptions
import os
import sys
import argparse
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
parser = argparse.ArgumentParser(description='gbk-nt_query')
parser.add_argument(
    '--virus', '-v', 
    choices=['sars2', 'hcmv'], 
    required=True, 
    help = 'Virus'
)
parser.add_argument(
    'input', 
    help='Input file'
)
args = vars(parser.parse_args())


if len(args['input']) < 2:
    raise Exception('no input')

dirname = os.path.dirname(__file__)
if args['virus'] == 'hcmv':
    file = os.path.join(dirname, "data/NC_006273.2.fasta")
    genbank = os.path.join(dirname, "data/NC_006273.2.gbk")
elif args['virus'] == 'sars2':
    file = os.path.join(dirname, "data/NC_045512.2.fasta")
    genbank = os.path.join(dirname, "data/NC_045512.2-mod.gbk")

product = position_product.position_product(int(args['input']), genbank, file)
nucleotide = position_nucleotide.position_nucleotide(int(args['input']), file)
protein = position_protein.position_protein(int(args['input']), genbank)

print(f"the position {args['input']} is in the {product}, the nucleotide is {nucleotide} and the amino acid is {protein}")