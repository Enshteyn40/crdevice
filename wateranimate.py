import os

# Joriy skriptning joylashuvini topamiz
current_dir = os.path.dirname(os.path.abspath(__file__))

# Bitta yuqoridagi papkani olamiz
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# phone.csv fayliga yo'l yaratamiz
csv_file_path = os.path.join(parent_dir, 'phone.csv')

# phone.csv faylining mavjudligini tekshiramiz
if os.path.exists(csv_file_path):
    print(f"Fayl topildi: {csv_file_path}")
else:
    print("phone.csv fayli topilmadi.")
