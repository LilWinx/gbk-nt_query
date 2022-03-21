def fnaconvert(data): #function to remove only the > at the start of every fasta
    """
    function for a later function that makes the fasta file a list. 
    Looks like this:
    ['A', 'C', 'A', 'T', 'A', 'A', 'G']
    """
    with open(data, 'r') as oldfasta:
        lines = oldfasta.readlines()
        oneline = ""
        for line in lines:
            if not line.startswith('>'):
                oneline += line.replace('\n', '') # delete all the line breaks
        return list(oneline) # this outputs each nucleotide into a list.

def fna_length(data):
    """
    function for a later function that counts the number of characters in the fasta file
    """
    with open(data, 'r') as oldfasta:
        lines = oldfasta.readlines()
        oneline = ""
        for line in lines:
            if not line.startswith('>'):
                oneline += line.replace('\n', '') # delete all the line breaks
        return len(oneline) # return the length of the line
#len(oneline)