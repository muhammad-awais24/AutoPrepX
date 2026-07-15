import pandas as pd

def handle_missing(df):
    df = df.copy()
    
    # Age ko median se fill karein
    if 'age' in df.columns:
        df['age'] = df['age'].fillna(df['age'].median())
        
    # Fare ko median se fill karein
    if 'fare' in df.columns:
        df['fare'] = df['fare'].fillna(df['fare'].median())
        
    # Embarked ko mode (most frequent) se fill karein
    if 'embarked' in df.columns:
        df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
        
    return df