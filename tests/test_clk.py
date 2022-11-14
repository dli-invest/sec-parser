import sys
sys.path.append('../sec_parser')
sys.path.append('..')
from sec_parser.clk import get_list_of_ciks

def test_clk():
    df = get_list_of_ciks()
    assert len(df) > 3

def test_zim_in_clk():
    df = get_list_of_ciks()
    assert df[df['ticker'] == 'ZIM'].iloc[0]['cik'] == '0001654126'