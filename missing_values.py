import pandas as pd

df = pd.read_csv(r"c:\Users\kalpa\Desktop\aiml-crash-kalpana\missing_data.csv")

print("Missing Values Count:")
print(df.isnull().sum())

print("\nAfter dropna():")
print(df.dropna())

print("\nAfter fillna(0):")
print(df.fillna(0))