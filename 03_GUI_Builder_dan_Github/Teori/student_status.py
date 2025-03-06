from enum import Enum 

class StatusMahasiswa(Enum):
    TERDAFTAR = "Terdaftar"
    AKTIF = "Aktif"
    LULUS = "Lulus"
    CUTI = "Cuti"

class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    LULUS = "Lulus"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"


transition = {
    StatusMahasiswa.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StatusMahasiswa.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StatusMahasiswa.CUTI,
    },
    StatusMahasiswa.AKTIF: {                        
        TriggerInputState.LULUS: StatusMahasiswa.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StatusMahasiswa.CUTI,
    },
    StatusMahasiswa.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StatusMahasiswa.AKTIF,
    },
}

def change_state(current_state, trigger_input):
    if current_state  in transition and trigger_input  in transition[current_state]:
        return "Transis tidak valid"
    return transition[current_state][trigger_input]

current_state = StatusMahasiswa.TERDAFTAR
next_state = change_state(current_state, TriggerInputState.CETAK_KSM)
print(f"Status mahasiswa saat ini: {current_state.value}")