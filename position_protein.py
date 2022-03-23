import numpy as np
import genbankconvert
import pandas as pd

def position_protein(position, genbank):
    df = pd.DataFrame(genbankconvert.genbankconvert(genbank), columns = ['together'])
    intbase = df['together'].str.split(',', expand=True)
    intbase.columns = ['product', 'start', 'end', 'sequence']
    database = intbase.astype({'start': int, 'end': int}) # converts the start and end into integers for the fucking IF statement.
    out_sequence = None 
    out_aa = "non-coding"
    codon_position = np.NaN
    for row in database.itertuples():
        if row.start < position <= row.end:
            out_sequence = row.sequence
            start_position = row.start
            break
    if out_sequence != None:
        codon_position = int((position - (start_position + 1)) /3)
        for index, amino_acid in enumerate(list(out_sequence)):
            if codon_position == index:
                out_aa = amino_acid
                break
    return f"{out_aa} on codon {codon_position + 1}"

