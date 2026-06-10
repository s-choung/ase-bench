from ase import Atoms, Atom
from ase.build import fcc111, molecule
from ase.visualize import view

# Create Al(111) 3-layer slab
al_slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Create N2 molecule
n2 = molecule('N2')

# Position N2 on bridge site at 2.0 angstroms
bridge_site = al_slab.positions[1]  # Assuming bridge site is between atoms 0 and 1
bridge_site[2] += 2.0
n2.translate(bridge_site - n2.positions[0])

# Combine slab and N2
final_structure = al_slab + n2

# Print number of atoms and atom types
print(f"Number of atoms: {len(final_structure)}")
print(f"Atom types: {final_structure.get_chemical_symbols()}")

# Optional: view the structure
# view(final_structure)
