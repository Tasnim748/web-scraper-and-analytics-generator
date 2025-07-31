import pandas as pd
import numpy as np
import re

def clean_price_value(value):
    """
    Clean price values by removing currency symbols and other non-numeric characters.
    
    Parameters:
    -----------
    value : str or numeric
        The value to clean
        
    Returns:
    --------
    float or np.nan
        Cleaned numeric value
    """
    if pd.isna(value) or value == "":
        return np.nan
    
    # If already numeric, return as is
    if isinstance(value, (int, float)):
        return value
        
    # For strings, remove currency symbols, commas, etc.
    if isinstance(value, str):
        # Remove currency symbols, spaces, commas, etc., keep numbers, decimal points and minus signs
        numeric_str = re.sub(r'[^\d.-]', '', value)
        try:
            return float(numeric_str) if numeric_str else np.nan
        except ValueError:
            return np.nan
    
    return np.nan

def convert_data_types(df, column_types):
    """
    Convert DataFrame columns to appropriate data types.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataframe to process
    column_types : dict
        Dictionary mapping column names to desired data types.
        Supported types: 'numeric', 'price', 'text', 'date', 'category', 'boolean'
    
    Returns:
    --------
    pandas.DataFrame
        DataFrame with converted column types
    """
    # Make a copy to avoid modifying the original dataframe
    df_clean = df.copy()
    
    for col, dtype in column_types.items():
        if col not in df_clean.columns:
            continue
            
        if dtype == 'numeric':
            # First try direct conversion to numeric
            try:
                df_clean[col] = pd.to_numeric(df_clean[col])
            except (ValueError, TypeError):
                # If direct conversion fails, apply clean_price_value function
                df_clean[col] = df_clean[col].apply(clean_price_value)
        elif dtype == 'date':
            # Convert to datetime
            df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')
        elif dtype == 'boolean':
            # Convert to boolean
            df_clean[col] = df_clean[col].map({'true': True, 'false': False, 
                                              'yes': True, 'no': False,
                                              '1': True, '0': False}, na_action='ignore')
        elif dtype == 'category':
            # Convert to category
            df_clean[col] = df_clean[col].astype('category')
    
    return df_clean

def remove_null_values(df, null_values=None, strategy='drop'):
    """
    Handle null values in DataFrame
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataframe to process
    null_values : list
        Custom values to consider as NaN
    strategy : str, default 'drop'
        Strategy to handle nulls: 'drop' or 'fill'
    
    Returns:
    --------
    pandas.DataFrame
        DataFrame with handled null values
    """
    # Make a copy to avoid modifying the original dataframe
    df_clean = df.copy()
    
    # Replace custom null values with NaN
    if null_values:
        for val in null_values:
            df_clean.replace(val, np.nan, inplace=True)
    
    # Handle empty strings in object columns
    for col in df_clean.select_dtypes(include=['object']).columns:
        df_clean[col] = df_clean[col].replace('', np.nan)
    
    # Strategy to handle nulls
    if strategy == 'drop':
        df_clean = df_clean.dropna()
    elif strategy == 'fill':
        # Fill numeric with mean
        for col in df_clean.select_dtypes(include=['number']).columns:
            df_clean[col].fillna(df_clean[col].mean(), inplace=True)
        
        # Fill categorical with mode
        for col in df_clean.select_dtypes(exclude=['number']).columns:
            df_clean[col].fillna(df_clean[col].mode()[0] if not df_clean[col].mode().empty else "", inplace=True)
    
    return df_clean