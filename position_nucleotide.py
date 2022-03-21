import fnaconvert

def position_nucleotide(position, file):
    out_nucleotide = 'outside of fasta file, are you sure you want this position?'
    for index, nucleotide in enumerate (fnaconvert.fnaconvert(file)):
        if position == index + 1:
            out_nucleotide = nucleotide
            break
    return out_nucleotide

"""
alternative one-liner cos you retarded
return fnaconvert.fnaconvert(file)[position-1]
"""