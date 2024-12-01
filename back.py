# Basis aturan untuk troubleshooting komputer
rules = {
    'Komputer Tidak Menyala': [
        {'syarat': 'PSU Rusak'},
        {'syarat': 'Kabel Daya Terlepas'}
    ],
    'Layar Tidak Menyala': [
        {'syarat': 'Monitor Rusak'},
        {'syarat': 'Kabel Monitor Terlepas'}
    ],
    'Kipas Tidak Berputar': [
        {'syarat': 'PSU Rusak'},
        {'syarat': 'Kabel Daya Terlepas'}
    ],
    'PSU Rusak': [
        {'syarat': 'Tidak Ada Daya'}
    ],
    'Kabel Daya Terlepas': [],
    'Monitor Rusak': [],
    'Kabel Monitor Terlepas': []
}

# Fakta yang diketahui
facts = {
    'Tidak Ada Daya': False,
    'PSU Rusak': False,
    'Kabel Daya Terlepas': True,  # Fakta: Kabel daya memang terlepas
    'Monitor Rusak': False,
    'Kabel Monitor Terlepas': False
}

# Fungsi untuk backward chaining
def backward_chaining(goal, rules, facts):
    # Jika goal adalah fakta yang sudah diketahui, cek nilainya
    if goal in facts:
        return facts[goal]

    # Jika goal ada di aturan, periksa apakah syarat-syaratnya terpenuhi
    if goal in rules:
        for syarat in rules[goal]:
            if not backward_chaining(syarat['syarat'], rules, facts):
                return False
        return True

    # Jika tidak ada aturan untuk goal, kita anggap tidak bisa dibuktikan
    return False

# Mencoba untuk membuktikan apakah 'Komputer Tidak Menyala'
goal = 'Komputer Tidak Menyala'
result = backward_chaining(goal, rules, facts)

if result:
    print(f"Kesimpulan: {goal} dapat terjadi berdasarkan fakta dan aturan.")
else:
    print(f"Kesimpulan: {goal} tidak dapat terjadi berdasarkan fakta yang ada.")
