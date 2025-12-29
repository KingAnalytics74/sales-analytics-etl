import pandas as pd

def load_data(path):
    """Load raw sales dataset."""
    return pd.read_csv(path)

def clean_data(df):
    """Clean and preprocess raw sales data."""
    
    # Convert order_date to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Convert quantity to integer
    df['quantity'] = df['quantity'].astype(int)

    # Drop discount_percentage
    if 'discount_percentage' in df.columns:
        df = df.drop(columns=['discount_percentage'])

    # Lowercase payment method
    df['payment_method'] = df['payment_method'].str.lower()

    return df
