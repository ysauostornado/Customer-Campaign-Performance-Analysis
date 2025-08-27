import pandas as pd
import ast

# 1. Load the raw data
events = pd.read_csv("C:/Users/arsen/Downloads/Offers/events.csv")
offers = pd.read_csv("C:/Users/arsen/Downloads/Offers/offers.csv")

# 2. Parse 'value' column into dictionary
def parse_value(val):
    try:
        return ast.literal_eval(val)
    except:
        return {}

events["value_dict"] = events["value"].apply(parse_value)

# 3. Extract offer_id, amount, and reward
def extract_offer_id(row):
    return row["value_dict"].get("offer id") or row["value_dict"].get("offer_id")

def extract_amount(row):
    return row["value_dict"].get("amount") if row["event"] == "transaction" else None

def extract_reward(row):
    return row["value_dict"].get("reward") if row["event"] == "offer completed" else None

events["offer_id"] = events.apply(extract_offer_id, axis=1)
events["amount"] = events.apply(extract_amount, axis=1)
events["reward"] = events.apply(extract_reward, axis=1)

# 4. Keep only cleaned relevant columns
events_cleaned = events[["customer_id", "event", "time", "amount", "offer_id", "reward"]]

# 5. Save cleaned file (optional)
events_cleaned.to_csv("cleaned_events_python.csv", index=False)

# 6. Merge with offer metadata
events_merged = events_cleaned.merge(offers, how="left", on="offer_id")

# 7. Filter only promo-related events
promo_events = events_merged[events_merged['event'].isin(['offer received', 'offer viewed', 'offer completed'])]

# 8. Analyze performance by offer type
offer_perf = (
    promo_events
    .groupby(['offer_type', 'event'])
    .size()
    .unstack(fill_value=0)
    .reset_index()
)

# 9. Add completion rate
offer_perf['completion_rate'] = (
    offer_perf.get('offer completed', 0) / offer_perf.get('offer received', 1)
).round(2)

# Display results
print(offer_perf)
