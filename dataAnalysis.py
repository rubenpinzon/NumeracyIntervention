
import pandas as pd

labels2q = {'Success': (1, 2), 'Interest': (3, 4, 5), 'Utility': (6, 13, 7), 'Mastery': (8, 9), 'Performance': (10, 11)}
reverse = 4

df = pd.read_csv('Survey Learning.csv')
questions = list(df.columns.values)

# calculate the total scores for each group concept.
groups = pd.DataFrame()
for name, q in labels2q.items():
    print('Concept {} with {} questions'.format(name, len(q)))
    totalScore = df[list(q)].sum(axis=1)
    groups[name] = totalScore

print(groups)
