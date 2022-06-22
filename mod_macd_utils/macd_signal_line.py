def get_macd_signal_line(data, short_window = 20, long_window = 50, signal_window = 12):
    """
    Get SMA, LMA, MACD, signal_line
    
    parameters
    -----------------------------
    short_window: short moving average size
    long_window: long moving average size
    signal_window: moving average size for signal line
    Output:
    Data frame with price, SMA, LMA, MACD, signal_line
    SMA: short moving average
    LMA: long moving average
    MACD: SMA - LMA
    signal_line: moving average of MACD
    """
    macd_data = data.copy()
    # Create the set of short and long simple moving average, MACD, signal line over the 
    # respective periods
    macd_data["SMA"] = macd_data['price'].rolling(window = short_window, center=False).mean()
    macd_data["LMA"] = macd_data['price'].rolling(window = long_window, center=False).mean()
    macd_data["MACD"] = macd_data['SMA'] - macd_data['LMA']
    macd_data['signal_line'] = macd_data['MACD'].rolling(window = signal_window).mean()
    return macd_data

