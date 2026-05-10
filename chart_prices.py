import pandas as pd
import matplotlib.pyplot as plt

# Load order items data
order_items = pd.read_csv('olist_order_items_dataset.csv')

# Create chart
plt.figure(figsize=(12, 6))
plt.hist(order_items['price'], bins=50, color='#e74c3c', edgecolor='black')
plt.title('Product Price Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Price ($)', fontsize=12)
plt.ylabel('Number of Items', fontsize=12)
plt.xlim(0, 500)
plt.tight_layout()
plt.savefig('chart3_price_distribution.png', dpi=300)
print("✅ Chart saved as 'chart3_price_distribution.png'")
plt.show()