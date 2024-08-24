# Import pustaka yang diperlukan
from pycaret.arules import *

# Mendapatkan data yang akan digunakan (misalnya data transaksi dari pycaret)
data = get_data('transactions')

# Inisialisasi dan konfigurasi setup untuk association rules
arules = setup(data = data, transaction_id = 'Transaction_ID', item_id = 'Item_ID', session_id = 123,
               ignore_items = ['None'])

# Membuat model association rules
model = create_model(metric='lift')

# Menampilkan aturan asosiasi
print(model)

# Menyimpan model jika diperlukan
save_model(model, 'association_rules_model')

# Menampilkan plot aturan asosiasi
plot_model(model, plot = 'association')

# Menampilkan aturan asosiasi dengan filter berdasarkan confidence
rules = get_rules(model, metric='confidence', min_threshold=0.7)
print(rules)