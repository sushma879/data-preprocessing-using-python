import pandas as pd
import numpy as np
d = pd.read_csv("data_1.csv")
df = pd.DataFrame(d)
print(df)
drop_null = df.dropna() # first way to handle
print("In Dropping null values") # Totally dropped
print(drop_null)
# Second way to handle missing values
# Replacing Null values with default values
notNull = df.fillna("default")
print("In Displaying notNull as Default values")
print(notNull)
#Identifying data redundancy and elimination

clean_data = "new_data.csv"

not NULL.to_csv(clean_data, index = 'False')

print("new_data.csv is Created")

df_cleaned = df.drop_duplicates()

print("Display unique values")

print(df_cleaned)

#Noise Detection Removal

data = pd.series([10, 20, 50, 1800, 1900,60])

print('series values')

print (data)

print('mean values')

print(data_mean())

print(data_data.mean())

Z_scores = (data_data.mean()) /data_std()
print(z_scores)

threshold = 1

filtered_data =data[np.abs (z_scores)<threshold)

print(filtered_data)
