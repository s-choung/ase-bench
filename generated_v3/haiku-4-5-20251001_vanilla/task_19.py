from ase import Atoms
from ase.geometry import get_distances
import numpy as np

# CO2 분자 생성
positions = np.array([
    [5.0, 5.0, 5.0],      # C at origin (cell center)
    [5.0, 5.0, 6.16],     # O at +1.16 Å
    [5.0, 5.0, 3.84]      # O at -1.16 Å
])

co2 = Atoms('CO2', positions=positions, cell=[10, 10, 10], pbc=False)

# 원자 간 거리 계산
d, D = get_distances(co2[0].position, co2[1:].position, cell=co2.cell, pbc=co2.pbc)

print("CO2 분자 구조:")
print(f"C-O 거리 1: {d[0]:.4f} Å")
print(f"C-O 거리 2: {d[1]:.4f} Å")
print(f"O-O 거리: {np.linalg.norm(co2[1].position - co2[2].position):.4f} Å")
