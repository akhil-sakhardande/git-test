import pandas as pd
df = pd.read_csv("imdb_1000.csv")
print(df.content_rating.value_counts())
