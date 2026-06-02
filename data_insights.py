import pandas as pd

df = pd.read_csv(r"c:\Users\kalpa\Desktop\aiml-crash-kalpana\students.csv")

print("Describe Output:")
print(df.describe())

print("\nValue Counts (Math Marks):")
print(df["math"].value_counts())

print("\nObservation:")
print("describe() shows summary statistics.")
print("value_counts() shows frequency of values.")