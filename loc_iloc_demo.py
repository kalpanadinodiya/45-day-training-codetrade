import pandas as pd

df = pd.read_csv(r"c:\Users\kalpa\Desktop\aiml-crash-kalpana\students.csv")

print("Using .loc")
print(df.loc[0:1, ["name", "math"]])

print("\nUsing .iloc")
print(df.iloc[0:2, 0:2])

print("\nDifference:")
print(".loc uses labels (row and column names)")
print(".iloc uses positions (row and column numbers)")