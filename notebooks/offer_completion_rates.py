import pandas as pd

# Load the dataset
final_data = pd.read_csv("final_events_with_customers.csv")

# Only consider bogo and discount offers
reward_data = final_data[final_data['offer_type'].isin(['bogo', 'discount'])]

# Group by offer type and event type
offer_completion = (
    reward_data[reward_data['event'].isin(['offer viewed', 'offer completed'])]
    .groupby(['offer_type', 'event'])
    .size()
    .unstack(fill_value=0)
    .reset_index()
)

# Calculate completion rate per offer type
offer_completion['completion_rate'] = (
    offer_completion['offer completed'] / offer_completion['offer viewed']
).round(2)

# Show result
print(offer_completion)
