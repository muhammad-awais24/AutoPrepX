import pandas as pd

def scale_data(df):
    df = df.copy()
    # Hum numbers ko decimals (0-1) mein scale nahi kar rahe taake output normal rahe
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df[col] = df[col].abs() # Ensure everything stays positive
    return df