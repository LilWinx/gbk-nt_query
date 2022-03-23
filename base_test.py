import unittest
import position_nucleotide
import test_learning
import fnaconvert
import position_product
import position_protein
import os

testfasta = os.path.join(os.path.dirname(__file__), r"data\NC_045512.2.fasta")
testgbk = os.path.join(os.path.dirname(__file__), r"data\NC_0045512.2-mod.gbk")

class TestSum(unittest.TestCase):
    def setUp(self):
        self.testfasta = testfasta
        self.testgbk = testgbk

    def test_position_product_input_2(self):
        result = position_product.position_product(30000, self.testgbk, self.testfasta)
        self.assertEqual(result, "outside of genome")
    
    def test_position_nucleotide_input(self):
        result = position_nucleotide.position_nucleotide(11670, self.testfasta)
        self.assertEqual(result, "G")

    def test_fnaconvert_fna_length(self):
        result = fnaconvert.fna_length(self.testfasta)
        self.assertEqual(result, 29903)

    def test_position_protein(self):
        result = position_protein.position_protein(28321, self.testgbk)
        self.assertEqual(result, "T")

    def test_position_product_input(self):
        result = position_product.position_product(11670, self.testgbk, self.testfasta)
        self.assertEqual(result, "nsp6")
