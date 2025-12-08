# Given a log file with `[timestamp, customer_id, webpage]`, 
# determine the top 3 most frequently visited 
# **sequences of 3 webpages** across all customers.

import pandas as pd

def mostFrequentlyVisitedSequencesOf3Webpages(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["customer_id", "timestamp"])
    
    df["next1"] = df.groupby("customer_id")["webpage"].shift(-1)
    df["next2"] = df.groupby("customer_id")["webpage"].shift(-2)
    
    df["seq3"] = df.apply(
        lambda r: ','.join([r['webpage'], r['next1'], r['next2']])
            if pd.notnull(r["next2"]) else None,
        axis=1
    )
    
    counts = df["seq3"].dropna().value_counts()
    
    counts = counts.reset_index()
    counts.columns = ["sequence", "count"]
    
    counts["rank"] = counts["count"].rank(method="first", ascending=False).astype(int)
    
    return counts.head(3)
    
# ============================================ #
# Example Input #

df = pd.DataFrame([
    ["2025-01-01 10:00", "1", "home"],
    ["2025-01-01 10:01", "1", "products"],
    ["2025-01-01 10:02", "1", "cart"],

    ["2025-01-01 11:00", "1", "home"],
    ["2025-01-01 11:01", "1", "products"],
    ["2025-01-01 11:02", "1", "cart"],

    ["2025-01-01 12:00", "2", "home"],
    ["2025-01-01 12:01", "2", "search"],
    ["2025-01-01 12:02", "2", "results"],
    ["2025-01-01 12:03", "2", "productPage"],
    
    ["2025-01-01 11:00", "2", "home"],
    ["2025-01-01 11:01", "2", "products"],
    ["2025-01-01 11:02", "2", "cart"],
    
    ["2025-01-01 11:00", "1", "home"],
    ["2025-01-01 11:01", "3", "products"],
    ["2025-01-01 11:02", "1", "cart"],
], columns=["timestamp", "customer_id", "webpage"])

print(mostFrequentlyVisitedSequencesOf3Webpages(df))