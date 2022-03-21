from doctest import OutputChecker
import pandas as pd
import numpy as np
import genbankconvert
import fnaconvert

"""
Takes the genbankconvert output and makes it into a dataframe (obviously can do this without pandas but what the heck, this is what i know)
The gbk file is filtered for its product (name of gene), the start and end positions, and the protein sequence which is used in position_protein

"""

def position_product(position, genbank, file):
    df = pd.DataFrame(genbankconvert.genbankconvert(genbank), columns = ['together'])
    intbase = df['together'].str.split(',', expand=True)
    intbase.columns = ['product', 'start', 'end', 'sequence']
    database = intbase.astype({'start': int, 'end': int}) # converts the start and end into integers for the fucking IF statement.
    out_product = 'intergenic region' # makes it default to intergenic region if the if statement is not met.
    for row in database.itertuples():
        if row.start < position <= row.end: # this needs to be < and <= because I don't want it to include the start position (cos its shifted one) CONFIRMED ON GENEIOUS PRIME
            out_product = row.product # don't fucking print here retard.
            break
    if fnaconvert.fna_length(file) < position:
        out_product = "outside of genome"
    return out_product


