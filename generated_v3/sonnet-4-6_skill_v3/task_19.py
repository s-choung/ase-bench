from ase import Atoms
from ase.geometry import get_distances

co2 = Atoms(
    symbols=['O', 'C', 'O'],
    positions=[
        [-1.16, 0.0, 0.0],
        [ 0.00, 0.0, 0.0],
        [ 1.16, 0.0, 0.0],
    ],
    cell=[10, 10, 10],
    pbc=False,
)

D, d = get_distances(co2.positions)

print("원자 간 거리 행렬 (Å):")
symbols = co2.get_chemical_symbols()
for i in range(len(co2)):
    for j in range(i+1, len(co2)):
        print(f"  {symbols[i]}({i}) — {symbols[j]}({j}): {d[i, j]:.4f} Å")
