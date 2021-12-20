import os
import pandas as pd
s = os.path.join("https://archive.ics,uci.edu", "ml", "machine-learning-databases", "iris", "iris.data")
print('URL : ', s)

df = pd.read_csv(s, header=None, encoding="UTF-8")
df.tail()