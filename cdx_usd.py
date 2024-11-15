import requests
import pandas as pd
from io import StringIO

def get_cdx_usd_revenue_df():
    
    df = pd.DataFrame()

    url = 'https://api.dune.com/api/v1/query/4289320/results/csv'
    headers = {
        'X-Dune-API-Key': ''
    }
    params = {
        'limit': 25000
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        # Convert the CSV string data to a pandas DataFrame
        df = pd.read_csv(StringIO(response.text))
        df['day'] = pd.to_datetime(df['day']).dt.strftime('%Y-%m-%d')
        
        # Optional: Display first few rows to verify the data
        print(df.head())
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    return df

df = get_cdx_usd_revenue_df()
print(df)