import os

# Mendapatkan path ke folder saat ini (di mana skrip ini berada)
current_folder = os.path.dirname(os.path.abspath(__file__))

# Mendapatkan daftar nama file di folder saat ini
file_names = os.listdir(current_folder)

# Menampilkan nama file
for file_name in file_names:
    print(file_name)
