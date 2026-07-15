import pandas as pd

def remove_outliers(df):
    df = df.copy()
    
    # Sirf age aur fare par outlier removal lagayein
    for col in ['age', 'fare']:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Range ke bahar wali rows ko drop kar dein
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            
    return df