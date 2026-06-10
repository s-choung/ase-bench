from ase import Atoms
import numpy as np

# CO2: C at origin, O at ±1.16 Å along x
positions = [(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)]
symbols = ['C', 'O', 'O']

molecule = Atoms(symbols=symbols,
                 positions=positions,
                 cell=[10, 10, 10],
                 pbc=False)

# Interatomic distances
n = len(molecule)
for i in range(n):
    for j in range(i + 1, n):
        d, v = molecule.get_distances(i, j, mic=False, vector=True)
        print(f"Distance {molecule[i].symbol}-{molecule[j].symbol}: {d:.3f} Å")
