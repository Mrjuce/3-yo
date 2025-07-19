import panda as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df  = pd.read_csv("digitaledu_users.csv")
print("1) Початковий вигляд даних(5 перших рядків):")
print(df.head())
print("\nІнформація про типи та пропуски:")
print(df.info())



df  = df.drop(columns = ["id", "Last_seen"])
print("\n2) Після видалення 'id' і 'last_seen': ")



def convert_bdate(bdate):
    try:
        parts = bdate.split(".")
        if len(parts) == 3:
            day, month, year = map(int,parts)
            return 2025 - year
    except:
        return np.nan
    
