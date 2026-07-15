import pandas as pd
from preprocessing.missing import handle_missing
from preprocessing.outliers import remove_outliers
from preprocessing.encoding import encode_data
from preprocessing.scaling import scale_data

def run_parallel(df):
    df = df.copy()
    
    # Columns ko lowercase karein taake matching mein galti na ho
    df.columns = [c.lower() for c in df.columns]
    
    # =========================================================================
    # UPDATE: Humne yahan se 'name' ko nikal diya hai taake naam drop na hon!
    # =========================================================================
    cols_to_drop = ['passengerid', 'ticket', 'cabin']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors='ignore')
        
    # 2. Preprocessing Steps run karein
    df = handle_missing(df)
    df = remove_outliers(df)
    df = encode_data(df)  # Yeh text columns (Sex, Embarked, Name) ko text hi rakhega
    df = scale_data(df)   # Yeh sirf numeric columns ko positive rakhega
    
    return df