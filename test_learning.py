def fna_test(data): #function to remove only the > at the start of every fasta
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
        return oneline     