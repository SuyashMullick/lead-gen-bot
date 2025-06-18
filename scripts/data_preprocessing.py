import pandas as pd

df = pd.read_csv("data/companies.csv")

print(f"Initial dataset size: {len(df)} rows")

df_clean = df.dropna(subset=['description'])
df_clean = df_clean[df_clean['description'].str.strip() != '']

print(f"After removing missing descriptions: {len(df_clean)} rows")

df_sample = df_clean.head(10)

df_sample.to_csv("data/companies_cleaned.csv", index=False)

df_sample.to_json("data/companies_cleaned.json", orient="records", indent=2)

print("Cleaned sample saved to companies_cleaned.csv and .json")
