import sys
import unittest

sys.path.append("..")
sys.path.append("../parser")

from .clk import get_list_of_ciks



class TestClk(unittest.TestCase):

    def test_clk():
        df = get_list_of_ciks()
        assert len(df) > 3

    def test_zim_in_clk():
        df = get_list_of_ciks()
        assert df[df['ticker'] == 'ZIM'].iloc[0]['cik'] == '0001654126'

if __name__ == '__main__':
    unittest.main()