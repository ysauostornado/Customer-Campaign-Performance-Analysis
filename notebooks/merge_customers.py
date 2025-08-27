import pandas as pd
import ast

# 1. Load the cleaned datasets
events_cleaned = pd.read_csv("cleaned_events_python.csv")  # From earlier step
offers = pd.read_csv("C:/Users/arsen/Downloads/Offers/offers.csv")
customers_cleaned = pd.read_csv("C:/Users/arsen/Downloads/Offers/valid_customers.csv")     # Your uploaded filtered customer data

# 2. Merge events with offers (on offer_id)
events_merged = events_cleaned.merge(offers, how="left", on="offer_id")

# 3. Merge with cleaned customers (on customer_id)
final_data = events_merged.merge(customers_cleaned, how="inner", on="customer_id")

# 4. Export the final combined dataset for Tableau or Excel
final_data.to_csv("final_events_with_customers.csv", index=False)

# Optional: Preview
print(final_data.head())

# --- CAMPAIGN METRICS INSIGHTS ---

# Total Revenue from all transactions
total_revenue = final_data[final_data['event'] == 'transaction']['amount'].sum()

# Total value of rewards given (cost to company)
total_rewards = final_data[final_data['event'] == 'offer completed']['reward_x'].sum()

# Net revenue = revenue - rewards
net_revenue = total_revenue - total_rewards

# Step 1: Filter only BOGO and Discount offer-related events
reward_events = final_data[
    (final_data['offer_type'].isin(['bogo', 'discount'])) &
    (final_data['event'].isin(['offer received', 'offer completed']))
]

# Step 2: Unique customers who received at least one BOGO or Discount offer
received_customers = reward_events[reward_events['event'] == 'offer received']['customer_id'].unique()

# Step 3: Unique customers who completed at least one BOGO or Discount offer
completed_customers = reward_events[reward_events['event'] == 'offer completed']['customer_id'].unique()

# Step 4: Customer-level completion rate
completion_rate = len(set(completed_customers)) / len(set(received_customers))

# Total transactions in cleaned data
clean_tx = final_data[final_data['event'] == 'transaction']['customer_id'].nunique()

# Load original customer file (with invalid entries)
all_customers = pd.read_csv("C:/Users/arsen/Downloads/Offers/customers.csv")
all_customers_ids = all_customers['customer_id'].unique()

# Load original events
events = pd.read_csv("C:/Users/arsen/Downloads/Offers/events.csv")
tx_customers = events[events['event'] == 'transaction']['customer_id'].nunique()



#Total revenue from valid&invalid customers
events = pd.read_csv("C:/Users/arsen/Downloads/Offers/events.csv")

# Parse amount from transactions
events['value'] = events['value'].apply(ast.literal_eval)
events['amount'] = events.apply(lambda row: row['value'].get('amount') if row['event'] == 'transaction' else None, axis=1)

# Total revenue (all transactions)
total_revenue_all = events[events['event'] == 'transaction']['amount'].sum()
print(f"💰 Total Revenue (All Customers): ${total_revenue_all:,.2f}")


print(f"💡 Transactions from valid customers: {clean_tx}")
print(f"💡 Transactions from all customers: {tx_customers}")
print(f"🧍 Difference = likely invalid customer behavior")


# Print insights
print("\n--- CAMPAIGN METRICS ---")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Rewards Paid Out: ${total_rewards:,.2f}")
print(f"Net Revenue After Rewards: ${net_revenue:,.2f}")
print(f"Offer Completion Rate: {completion_rate:.2%}")
unique_customers = final_data['customer_id'].nunique()
print(f"🧍‍♂️ Unique Customers: {unique_customers}")


