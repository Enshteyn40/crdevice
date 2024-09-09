import sys
import csv

# phone.csv faylining to'liq yo'li parametr sifatida uzatiladi
if len(sys.argv) < 2:
    print("phone.csv faylining yo'li uzatilmagan.")
    sys.exit(1)

csv_file_path = sys.argv[1]

# Faylni ochib ma'lumotlarni o'qish
try:
    with open(csv_file_path, 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print(f"Jami: {len(phlist)} ta raqamlar mavjud")
except FileNotFoundError:
    print(f"phone.csv fayli topilmadi: {csv_file_path}")
    sys.exit(1)
