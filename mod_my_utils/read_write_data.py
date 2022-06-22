import pandas as pd
import pandas_datareader as web

def get_stock_csv(folder_name, symbol, index_col):
    """ 
    This is a method for reading stock data 
    Input Argument: 
    Folder name 
    Stock name 
    Column for indexing
    Output: 
    Stock data with date as index 
    """ 
    file_name = folder_name + "/" + symbol + ".csv" 
    data = pd.read_csv(file_name) 
    data[index_col] = pd.to_datetime(data[index_col]) 
    data = data.set_index(index_col)
    print("stock name: ", symbol) 
#     print("Stock data variables: ", data.columns) 
#     print(data.head()) 
    return data


def get_price_yahoo(symbol, data_source, start_date = "1/1/2010", end_date = "1/1/2011"):
    """
    Get high low open close volume adj close data for a stock within the range
    
    Parameters
    ----------------------
    symbol : The name of the stock
    
    data_source :  Name of the data source
    
    start_date : start date for the date range
    
    end_date : end date for the date range
    """
    stock_name = symbol + '.NS'
    data = web.DataReader(name = stock_name, data_source = data_source, start = start_date, end = end_date)
    print('stock name', symbol)
    return data
    
