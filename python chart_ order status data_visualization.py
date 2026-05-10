import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
orders = pd.read_csv('olist_orders_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')

# Simple chart 1: Order Status
plt.figure(figsize=(10, 6))
orders['order_status'].value_counts().plot(kind='bar', color='#3498db')
plt.title('Order Status Distribution', fontsize=14, fontweight='bold')
plt.ylabel('Count')
plt.xlabel('Status')
plt.tight_layout()
plt.savefig('chart1_order_status.png')
plt.show()


print("✅ Charts saved!")