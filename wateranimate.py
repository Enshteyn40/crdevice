import os

# Joriy faylning yo'lini chiqarish
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Joriy katalog:", current_dir)

# Bir pog'ona yuqoridagi katalog
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
print("Yuqoridagi katalog:", parent_dir)

# Fayl yo'lini ko'rsatish
csv_file_path = os.path.join(parent_dir, 'phone.csv')
print("Fayl yo'li:", csv_file_path)
