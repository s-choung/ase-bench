from ase import Atoms
from ase.geometry import get_distances

# Create CO2 molecule manually
# C at (0,0,0), O at (-1.16, 0, 0) and (1.16, 0, 0)
atoms = Atoms(symbols=['C', 'O', 'O'], 
              positions=[[0, 0, 0], [-1.16, 0, 0], [1.16, 0, 0]])

# Set cell and periodic boundary conditions
atoms.set_cell([10, 10, 10])
atoms.set_pbc(False)

# Calculate interatomic distances
distances = get_distances(atoms.get_positions(), atoms.get_positions())

print(f"Atoms:\n{atoms}")
print(f"Distances matrix (Å):\n{distances}")
