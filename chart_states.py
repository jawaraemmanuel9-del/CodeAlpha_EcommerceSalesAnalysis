import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
order_items = pd.read_csv('olist_order_items_dataset.csv')
customers = pd.read_csv('olist_customers_dataset.csv')

# Chart 1: Top 10 States by Customers
plt.figure(figsize=(12, 6))
top_states = customers['customer_state'].value_counts().head(10)
top_states.plot(kind='barh', color='#2ecc71')
plt.title('Top 10 States by Customer Count', fontsize=14, fontweight='bold')
plt.xlabel('Number of Customers')
plt.tight_layout()
plt.savefig('chart2_top_states.png', dpi=300)
plt.show()

# Chart 2: Price Distribution
plt.figure(figsize=(12, 6))
plt.hist(order_items['price'], bins=50, color='#e74c3c', edgecolor='black')
plt.title('Product Price Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Price ($)')
plt.ylabel('Number of Items')
plt.xlim(0, 500)
plt.tight_layout()
plt.savefig('chart3_price_distribution.png', dpi=300)
plt.show()

# Chart 3: Shipping Cost Analysis
plt.figure(figsize=(12, 6))
plt.hist(order_items['freight_value'], bins=40, color='#f39c12', edgecolor='black')
plt.title('Shipping Cost Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Freight Value ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('chart4_shipping_costs.png', dpi=300)
plt.show()

print("✅ All charts created and saved!")