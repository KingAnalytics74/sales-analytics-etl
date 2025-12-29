from clean import load_data, clean_data
from transform import engineer_features
from analytics import (
    product_profitability, region_summary, weekend_vs_weekday,
    orders_by_day, orders_by_month, orders_by_size,
    top_products_by_size, region_sales, orders_by_weekday,
    shipping_costs
)

def main():
    # Load raw data
    df = load_data("data/dataset.csv")

    # Clean data
    df = clean_data(df)

    # Transform data
    df = engineer_features(df)

    # Run analytics and save outputs
    product_profitability(df).to_csv("outputs/product_profitability.csv", index=False)
    region_summary(df).to_csv("outputs/region_summary.csv", index=False)
    weekend_vs_weekday(df).to_csv("outputs/weekend_vs_weekday.csv", index=False)
    orders_by_day(df).to_csv("outputs/orders_by_day.csv", index=False)
    orders_by_month(df).to_csv("outputs/orders_by_month.csv", index=False)
    orders_by_size(df).to_csv("outputs/orders_by_size.csv", index=False)
    top_products_by_size(df).to_csv("outputs/top_products_by_size.csv", index=False)
    region_sales(df).to_csv("outputs/region_sales.csv", index=False)

    # Special shipping analytics
    highest_shipping, top_shipping_product = shipping_costs(df)
    print("Highest shipping:", highest_shipping)
    print("Top shipping product:", top_shipping_product)

if __name__ == "__main__":
    main()
