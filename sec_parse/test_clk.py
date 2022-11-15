import sys
from sec_parse.clk import get_list_of_ciks

def test_clk():
    df = get_list_of_ciks()
    assert len(df) > 3

def test_zim_in_clk():
    df = get_list_of_ciks()
    print(df)
    assert df[df['ticker'] == 'zim'].iloc[0]['cik'] == 1654126
