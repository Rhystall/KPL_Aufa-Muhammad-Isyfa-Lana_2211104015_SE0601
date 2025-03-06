from enum import Enum 

class StatusCheckout(Enum):
    IDLE = "Idle"
    MENUNGGU_PRODUK = "Menunggu Produk"
    MENGELUARKAN_PRODUK = "Mengeluarkan Produk"
    SELESAI = "Selesai"

class TriggerInputState(Enum):
    MASUKKAN_UANG = "Masukkan Uang"
    PILIH_PRODUK = "Pilih Produk"
    KELUARKAN_PRODUK = "Keluarkan Produk"
    RESET = "Reset"

# Transisi state
transition = {
    StatusCheckout.IDLE: {
        TriggerInputState.MASUKKAN_UANG: StatusCheckout.MENUNGGU_PRODUK,
    },
    StatusCheckout.MENUNGGU_PRODUK: {
        TriggerInputState.PILIH_PRODUK: StatusCheckout.MENGELUARKAN_PRODUK,
    },
    StatusCheckout.MENGELUARKAN_PRODUK: {
        TriggerInputState.KELUARKAN_PRODUK: StatusCheckout.SELESAI,
    },
    StatusCheckout.SELESAI: {
        TriggerInputState.RESET: StatusCheckout.IDLE,
    }
}

def change_state(current_state, trigger_input):
    if current_state not in transition or trigger_input not in transition[current_state]:
        return "Transisi tidak valid"
    return transition[current_state][trigger_input]

# Status awal
current_state = StatusCheckout.IDLE
print(f"Status produk saat ini: {current_state.value}")

# Transisi ke status berikutnya
next_state = change_state(current_state, TriggerInputState.MASUKKAN_UANG)

if isinstance(next_state, StatusCheckout):
    current_state = next_state
    print(f"Status produk setelah transisi: {current_state.value}")
else:
    print(next_state)  # Cetak pesan error jika transisi tidak valid
