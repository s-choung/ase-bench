from ase import Atoms
import numpy as np

# Lattice parameters
a = 2.95
c = a * 1.59

# HCP lattice vectors
cell = [
    [a, 0, 0],
    [a/2, a*np.sqrt(3)/2, 0],
    [0, 0, c]
]

# Atomic positions in fractional coordinates
positions = [
    [0, 0, 0],
    [1/3, 2/3, 1/2]
]

# Create Ti HCP structure
ti_hcp = Atoms(
    symbols='Ti2',
    scaled_positions=positions,
    cell=cell,
    pbc=True
)

# Output
print("Cell vectors (Å):")
for i, vec in enumerate(ti_hcp.cell):
    print(f"a{i+1}: {vec}")

print("\nAtomic positions (Å):")
for i, pos in enumerate(ti_hcp.get_positions()):
    print(f"Ti{i+1}: {pos}")

print(f"\nNumber of atoms: {len(ti_hcp)}")
