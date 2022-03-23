from Bio import SeqIO

#genbank = r'C:\Users\Winkie\Downloads\MN908947-3.gbk'

def genbankconvert(data):
    out_list = []
    for record in SeqIO.parse(data, "genbank"):
        for feature in record.features:
            if feature.type == 'CDS' or feature.type == 'mat_peptide':
                assert len(feature.qualifiers['translation']) == 1
                out_list.append("%s,%s,%s,%s" % (
                    feature.qualifiers['product'][0],
                    feature.location.start,
                    feature.location.end,
                    feature.qualifiers['translation'][0]))
    return out_list

