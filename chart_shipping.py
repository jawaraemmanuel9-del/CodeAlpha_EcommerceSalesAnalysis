import pandas as pd
import matplotlib.pyplot as plt

# Load order items data
order_items = pd.read_csv('olist_order_items_dataset.csv')

# Create chart
plt.figure(figsize=(12, 6))
plt.hist(order_items['freight_value'], bins=40, color='#f39c12', edgecolor='black')
plt.title('Shipping Cost Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Freight Value ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('chart4_shipping_costs.png', dpi=300)
print("✅ Chart saved as 'chart4_shipping_costs.png'")
plt.show()