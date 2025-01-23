import pandas as pd
file_path="example.csv"
read=pd.read_csv(file_path)
print('first five rows of the data are')
print(read.head())