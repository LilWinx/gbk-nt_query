import unittest
import position_nucleotide
import test_learning
import fnaconvert
import position_product
import position_protein
import input

class TestSum(unittest.TestCase):
    def test_fnaconvert(self):
        result = test_learning.fna_test(r'C:\Users\Winkie\Downloads\test.fasta')
        self.assertEqual(result, "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA")

    def test_selective_removal(self):
        result = fnaconvert.fnaconvert(r'C:\Users\Winkie\Downloads\test1.fasta')
        self.assertNotEqual(result, ">")

    def test_position_nucleotide_input(self):
        result = position_nucleotide.position_nucleotide(11670, r'C:\Users\Winkie\Downloads\MN908947-3.fasta')
        self.assertEqual(result, "G")

    def test_position_product_input(self):
        result = position_product.position_product(11670, r'C:\Users\Winkie\Downloads\MN908947-3.gbk', r'C:\Users\Winkie\Downloads\MN908947-3.fasta')
        self.assertEqual(result, "orf1ab polyprotein")
    
    def test_position_product_input_2(self):
        result = position_product.position_product(30000, r'C:\Users\Winkie\Downloads\MN908947-3.gbk', r'C:\Users\Winkie\Downloads\MN908947-3.fasta')
        self.assertEqual(result, "outside of genome")

    def test_fnaconvert_fna_length(self):
        result = fnaconvert.fna_length(r'C:\Users\Winkie\Downloads\MN908947-3.fasta')
        self.assertEqual(result, 29903)
    
    def test_position_protein(self):
        result = position_protein.position_protein(28321, r'C:\Users\Winkie\Downloads\MN908947-3.gbk')
        self.assertEqual(result, "T")
    
    