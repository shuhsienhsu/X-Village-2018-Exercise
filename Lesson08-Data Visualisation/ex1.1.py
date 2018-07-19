import pandas as pd
import numpy as np

table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]
df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])
# print(something) # total score
print(df.groupby('class').sum())
# print(something) # mean score
print(df.groupby('class').mean())
# print(something) # correlation coefficient
print(df.groupby('class')[['math_score','eng_score']].corr())
print(df.groupby('class')[['math_score','eng_score']].corr().ix[1::2,'math_score'])