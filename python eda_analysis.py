import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
orders = pd.read_csv('olist_orders_dataset.csv')
customers = pd.read_csv('olist_customers_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')

print("="*50)
print("E-COMMERCE EXPLORATORY DATA ANALYSIS")
print("="*50)

# CUSTOMER ANALYSIS
print("\n1. CUSTOMER OVERVIEW:")
print(f"Total Customers: {customers.shape[0]}")
print(f"Total Orders: {orders.shape[0]}")
print(f"Total Items Sold: {order_items.shape[0]}")

# ORDER STATUS DISTRIBUTION
print("\n2. ORDER STATUS BREAKDOWN:")
print(orders['order_status'].value_counts())

# REVENUE ANALYSIS
print("\n3. REVENUE INSIGHTS:")
total_revenue = order_items['price'].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")
avg_order_value = total_revenue / orders.shape[0]
print(f"Average Order Value: ${avg_order_value:,.2f}")

# CUSTOMER LOCATION DISTRIBUTION
print("\n4. TOP 10 STATES BY CUSTOMERS:")
print(customers['customer_state'].value_counts().head(10))

# PRODUCT ANALYSIS
print("\n5. TOP 10 MOST SOLD PRODUCTS:")
top_products = order_items.groupby('product_id')['order_id'].count().sort_values(ascending=False).head(10)
print(top_products)

# PRICE ANALYSIS
print("\n6. PRICE STATISTICS:")
print(f"Average Item Price: ${order_items['price'].mean():,.2f}")
print(f"Max Price: ${order_items['price'].max():,.2f}")
print(f"Min Price: ${order_items['price'].min():,.2f}")

# SHIPPING ANALYSIS
print("\n7. FREIGHT VALUE ANALYSIS:")
print(f"Total Shipping Cost: ${order_items['freight_value'].sum():,.2f}")
print(f"Average Shipping per Item: ${order_items['freight_value'].mean():,.2f}")

print("\n✅ Analysis Complete!")