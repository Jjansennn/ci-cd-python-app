# Fitur Aplikasi:
# input angka
# output:
# Genap / Ganjil

def check_number(n):
    if n % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"


if __name__ == "__main__":
    print(check_number(4))
