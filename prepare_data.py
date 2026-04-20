import pandas as pd

df = pd.read_csv('facebook_combined.txt', sep=' ', names=['source','target'])
df.to_csv('edges.csv', index=False)

nodes = pd.DataFrame({'id': pd.concat([df['source'], df['target']]).unique()})
nodes.to_csv('nodes.csv', index=False)

print(f'Relations : {len(df)}')
print(f'Noeuds    : {len(nodes)}')
