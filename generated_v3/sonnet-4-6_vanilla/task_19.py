from ase import Atoms
import numpy as np

co2 = Atoms(
    symbols=['C', 'O', 'O'],
    positions=[
        [0.0, 0.0, 0.0],
        [1.16, 0.0, 0.0],
        [-1.16, 0.0, 0.0]
    ],
    cell=[10.0, 10.0, 10.0],
    pbc=False
)

print("=== CO2 Molecule ===")
print(f"Symbols : {co2.get_chemical_symbols()}")
print(f"Positions:\n{co2.get_positions()}")
print(f"Cell    : {co2.get_cell().diagonal()}")
print(f"PBC     : {co2.get_pbc()}")

from ase.geometry import get_distances

pos = co2.get_positions()
cell = co2.get_cell()
pbc = co2.get_pbc()

_, D = get_distances(pos, cell=cell, pbc=pbc)

symbols = co2.get_chemical_symbols()
n = len(co2)

print("\n=== Interatomic Distances (Angstrom) ===")
for i in range(n):
    for j in range(i+1, n):
        print(f"  {symbols[i]}({i}) - {symbols[j]}({j}) : {D[i][j]:.6f} Å")
