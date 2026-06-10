import numpy as np
from ase.build import fcc111, molecule

# Create Al(111) slab with 3 layers
slab = fcc111('Al', size=(1, 1, 3), a=4.05)

# Add vacuum of 10 angstroms along z
slab.center(vacuum=10, axis=2)

# Find bridge site on the surface
z_coords = slab.positions[:, 2]
top_atoms = slab.positions[z_coords == z_coords.max()]
bridge_site = (top_atoms[0] + top_atoms[1]) / 2

# Get N2 molecule and set its center at the bridge site at height 2.0 angstroms
mol = molecule('N2')
surface_z = slab.positions[:, 2].max()
mol_center = np.array([bridge_site[0], bridge_site[1], surface_z + 2.0])
mol.positions = mol.positions - mol.get_center_of_mass() + mol_center

# Combine slab and molecule
final = slab + mol

# Print number of atoms and atom types
print(f"Number of atoms: {len(final)}")
print(f"Atom types: {final.get_chemical_symbols()}")
