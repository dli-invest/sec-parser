# parses ciks from the SEC Edgar database
import os
import pandas as pd
from constants import ticker_url

def get_list_of_ciks(sec_url: str = ticker_url) -> pd.DataFrame:
    """
        Parses ciks from the SEC Edgar database.
        Downloads ticker.txt as csv file from the SEC Edgar database.
        If the file is not present, it is downloaded.
        
    """
    # make sure cik_tickers.txt does not exist
    if os.path.exists('cik_tickers.txt'):
        # need to pad zeros until the length is 10, or could do that during use
        return pd.read_csv('cik_tickers.txt', sep='\t', header=None, names=['ticker', 'cik'])
    # read ticker.txt from SEC Edgar database
    df = pd.read_csv(sec_url, sep='\t', header=None, names=['ticker', 'cik'])
    # pad zeros until the length is 10
    df['cik'] = df['cik'].apply(lambda x: str(x).zfill(10))
    # save to file
    df.to_csv('cik_tickers.txt', sep='\t', index=False)
    return df

# df = get_list_of_ciks()