from os.path import abspath, dirname, join
import unittest
from csv_to_tmx import createTMX

dirpath = dirname(abspath(__file__))

csvpath = join(dirpath, 'sample.csv')
print("csvpath:", csvpath)

class TestCSVtoTMX(unittest.TestCase):

    def test_conversion(self):
        print(createTMX)
        createTMX(source_file=csvpath, output_file='./sample.tmx', srclang='zh-tw', targetlang='en')

