import pandas as pd

def engineer_features(df):
    """Create new calculated fields and date features."""

    # Total price
    df['total_price'] = df['quantity'] * df['price_per_unit']

    # Final amount paid
    df['final_amount_paid'] = df['total_price'] + df['shipping_cost']

    # Date features
    df['order_year'] = df['order_date'].dt.year
    df['order_month'] = df['order_date'].dt.month
    df['order_day'] = df['order_date'].dt.day
    df['order_weekday'] = df['order_date'].dt.day_name()

    # Weekend flag
    df['is_weekend'] = df['order_weekday'].isin(['Saturday', 'Sunday'])

    # Order size category
    df['order_size'] = df['quantity'].apply(
        lambda x: 'Small' if x <= 2 else ('Medium' if x <= 5 else 'Large')
    )

    return df
