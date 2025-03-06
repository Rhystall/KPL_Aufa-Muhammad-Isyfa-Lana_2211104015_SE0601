from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    PEREMPUAN = 2

patients = []

def add_patients(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis kelamin harus PRIA atau PEREMPUAN")
    
    patients.append({
        "name": name,
        "gender": gender.name
    })
    print(f"Berhasil menambahkan pasien {name} dengan jenis kelamin {gender.name}")

add_patients("Andi", JenisKelamin.PRIA)
add_patients("Siti", JenisKelamin.PEREMPUAN)
add_patients("Aziz", JenisKelamin.Trans)
