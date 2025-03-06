import time 
from enum import Enum 

# State 
class TrafficLight(Enum):
    RED = "Merah"
    YELLOW = "Kuning"
    GREEN = "Hijau"

# Bagian dari transisi aatau perubahan state
state_transitions = {
    TrafficLight.RED: TrafficLight.GREEN,
    TrafficLight.YELLOW: TrafficLight.RED,
    TrafficLight.GREEN: TrafficLight.YELLOW
}

state_durations = {
    TrafficLight.RED: 10,
    TrafficLight.YELLOW: 5,
    TrafficLight.GREEN: 8
}

current_state = TrafficLight.RED
next_state = state_transitions[current_state]
print(f"Warna lampu lalu lintas saat ini: {current_state.value}")

while True: 
    print(f"Lampu {current_state.value} membutuhkan waktu {state_durations[current_state]} detik")
    time.sleep(state_durations[current_state])
    current_state = state_transitions[current_state]
    print(f"Warna lampu lalu lintas saat ini: {current_state.value}")
    print("")