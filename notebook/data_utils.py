import pandas as pd
def check_missing_data(df):

    """
    Function for identify the missing data in every column
    it returns a dataframe with count and percentage of NaN 
    """
    # counts the NaN value for every column
    missing_count = df.isnull().sum()
    
    # calculates the NaN percentage
    missing_percent = (df.isnull().sum() / len(df)) * 100
    
    missing_table = pd.concat([missing_count, missing_percent], axis=1)
    missing_table.columns = ['Missing valurd', '% of total']
    
    # Let's sort to see where more data is missing
    return missing_table.sort_values(by='% of total', ascending=False)