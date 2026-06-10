from ase.build import molecule
from ase.geometry import get_distances

atoms = molecule('CH4')

print(f"Formula: {atoms.get_chemical_formula()}")
print("Coordinates:\n", atoms.get_positions())

# CH4 has 5 atoms; bonds are between central C (0) and 4 H (1,2,3,4)
bonds = get_distances(atoms, atoms, indices=[[0, i] for i in range(1, 5)])
print("Bond lengths (C-H):", bonds.flatten())
