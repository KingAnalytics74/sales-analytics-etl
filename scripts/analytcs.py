import pandas as pd

def product_profitability(df):
    """Calculate profitability metrics per product."""
    result = (
        df.groupby('product_id')
          .agg({
              'total_price': 'sum',
              'shipping_cost': 'sum',
              'final_amount_paid': 'sum'
          })
          .reset_index()
    )

    result['profit'] = result['final_amount_paid'] - result['shipping_cost']
    return result.sort_values(by='profit', ascending=False)


def region_summary(df):
    """Region-level sales and shipping metrics."""
    result = (
        df.groupby('region')
          .agg({
              'final_amount_paid': 'sum',
              'quantity': 'sum',
              'shipping_cost': 'sum'
          })
          .reset_index()
    )

    result['avg_order_value'] = (
        result['final_amount_paid'] / result['quantity']
    )

    return result


def weekend_vs_weekday(df):
    """Compare weekend and weekday sales."""
    result = (
        df.groupby('is_weekend')
          .agg({
              'final_amount_paid': 'sum',
              'quantity': 'sum',
              'order_id': 'count'
          })
          .reset_index()
    )

    result['day_type'] = result['is_weekend'].map({
        True: 'Weekend',
        False: 'Weekday'
    })

    return result


def orders_by_day(df):
    """Orders per day of month."""
    return df.groupby('order_day')['order_id'].count().reset_index()


def orders_by_month(df):
    """Orders per month."""
    return df.groupby('order_month')['order_id'].count().reset_index()


def orders_by_size(df):
    """Orders per size category."""
    return df.groupby('order_size')['order_id'].count().reset_index()


def top_products_by_size(df):
    """Top products per order size."""
    result = (
        df.groupby(['order_size', 'product_id'])['order_id']
          .count()
          .reset_index(name='order_count')
    )

    return result.sort_values(['order_size', 'order_count'], ascending=[True, False])


def region_sales(df):
    """Total sales per region."""
    return (
        df.groupby('region')['final_amount_paid']
          .sum()
          .reset_index(name='total_sales')
    )


def orders_by_weekday(df):
    """Orders per weekday."""
    return (
        df.groupby('order_weekday')['order_id']
          .count()
          .reset_index(name='order_count')
    )


def shipping_costs(df):
    """Shipping cost analytics."""
    highest_shipping = df.loc[df['shipping_cost'].idxmax()]

    shipping_by_product = (
        df.groupby('product_id')['shipping_cost']
          .sum()
          .reset_index(name='total_shipping_cost')
    )

    top_shipping_product = shipping_by_product.loc[
        shipping_by_product['total_shipping_cost'].idxmax()
    ]

    return highest_shipping, top_shipping_product
