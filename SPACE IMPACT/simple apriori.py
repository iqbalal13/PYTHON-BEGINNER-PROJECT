import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Membuat DataFrame dengan data transaksi
data = {'T1': [1, 1, 1, 0, 0],
        'T2': [1, 1, 0, 1, 0],
        'T3': [1, 0, 1, 1, 0],
        'T4': [0, 1, 1, 0, 1],
        'T5': [1, 1, 1, 0, 1]}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E']).T

# Menampilkan DataFrame
print("DataFrame Transaksi:")
print(df)

# Menggunakan algoritma Apriori untuk menemukan itemset yang sering muncul
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

# Menampilkan itemset yang sering muncul
print("\nItemset yang sering muncul:")
print(frequent_itemsets)

# Menghasilkan aturan asosiasi dari itemset yang sering muncul
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Menampilkan aturan asosiasi
print("\nAturan Asosiasi:")
print(rules)