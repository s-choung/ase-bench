from ase import Atoms
from ase.geometry import get_distances

# CO2 분자 수동 구성
positions = [
    [5.0, 5.0, 5.0],      # C at origin (cell center)
    [6.16, 5.0, 5.0],     # O at +1.16 Å
    [3.84, 5.0, 5.0],     # O at -1.16 Å
]
symbols = ['C', 'O', 'O']

co2 = Atoms(symbols, positions=positions, cell=[10, 10, 10], pbc=False)

# 원자 간 거리 계산
D, D_len = get_distances(co2.positions, cell=co2.get_cell(), pbc=co2.pbc)

print("Distance matrix:")
print(D_len)
print("\nC-O distances:")
print(f"C-O1: {D_len[0, 1]:.4f} Å")
print(f"C-O2: {D_len[0, 2]:.4f} Å")
print(f"O-O distance: {D_len[1, 2]:.4f} Å")
