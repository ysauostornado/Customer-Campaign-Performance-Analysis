import pandas as pd

# Load final cleaned dataset (valid customers only)
df = pd.read_csv("final_events_with_customers.csv")

# Filter relevant events
transactions = df[df['event'] == 'transaction']
offers_received = df[df['event'] == 'offer received']
offers_completed = df[df['event'] == 'offer completed']

# Merge received + completed offers per customer
offer_lifecycle = offers_received.merge(
    offers_completed,
    on=['customer_id', 'offer_id'],
    suffixes=('_received', '_completed'),
    how='inner'
)
print(offer_lifecycle.columns.tolist())

# Calculate expiration window
offer_lifecycle['offer_end_time'] = offer_lifecycle['time_received'] + offer_lifecycle['duration_received']


# Merge transactions with offers completed by same customer
merged = pd.merge(transactions, offer_lifecycle, on='customer_id', how='inner')

# Filter for transactions that happened during the offer period and match the offer_id
valid_tx = merged[
    (merged['time'] >= merged['time_received']) &
    (merged['time'] <= merged['offer_end_time']) &
    (merged['offer_id_x'] == merged['offer_id_y']) &
    (merged['offer_type'] != 'informational')
]

# Group by offer_type and sum revenue
result = valid_tx.groupby('offer_type')['amount'].sum().reset_index()
result = result.sort_values(by='amount', ascending=False)

# Print results
print("\n📊 Revenue by Offer Type (Valid Customers Only):")
print(result)