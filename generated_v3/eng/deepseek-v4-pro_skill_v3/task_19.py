from ase import Atoms
from ase.geometry import get_distances

# Build CO2: C at origin, O atoms at ±1.16 Å along x
positions = [[0.0, 0.0, 0.0],
             [1.16, 0.0, 0.0],
             [-1.16, 0.0, 0.0]]
atoms = Atoms('COO', positions=positions, cell=[10, 10, 10], pbc=False)

# Compute pairwise distances
distances, _ = get_distances(atoms.positions, atoms.positions, cell=atoms.cell, pbc=atoms.pbc)

# Print results
print("Interatomic distances (Å):")
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        print(f"{atoms[i].symbol}{i} - {atoms[j].symbol}{j}: {distances[i, j]:.3f} Å")
