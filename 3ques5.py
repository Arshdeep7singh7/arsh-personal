import pandas as pd
file_path = "example.csv"
df = pd.read_csv(file_path)


df = df.drop(index=3)
df = df.drop(df.columns[2], axis=1)

print("\nModified DataFrame (after deleting row 4 and column 3):")
print(df)
