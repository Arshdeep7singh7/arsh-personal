import pandas as pd
data={"tid":[1,2,3,4,5,6,7,8,9,10],
      "refund":["yes",'no','no','yes','no','no','yes','no','no','no'],
      "maritalstatus":["single",'married','single','married','divorced','married','divorced','single','married','single'],
      "taxableIncome":[125000,100000,70000,120000,95000,60000,220000,85000,75000,90000],
      "cheat":['no','no','no','no','yess','no','no','yes','no','yes']
      }
df=pd.DataFrame(data)
rows1=df.iloc[3:8]
print(rows1)
rows2=df.iloc[4:9,2:5]
print(rows2)
allrows=df.iloc[:,1:4]
print(allrows)