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
