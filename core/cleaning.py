# cleaning.py

import pandas as pd

def clean_data(csv_file, numeric_fields=None, strip_fields=None):
    df = pd.read_csv(csv_file)
    numeric_fields = numeric_fields or []
    strip_fields = strip_fields or []
    for field in numeric_fields:
        # Remove common currency symbols and commas, then convert to float
        df[field] = pd.to_numeric(
            df[field].astype(str).str.replace(r'[^\d.]', '', regex=True),
            errors='coerce'
        )
    for field in strip_fields:
        df[field] = df[field].astype(str).str.strip()
    df.dropna(inplace=True)
    return df