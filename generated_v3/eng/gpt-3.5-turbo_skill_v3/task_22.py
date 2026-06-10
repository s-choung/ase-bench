from ase.build import fcc111, add_adsorbate
from ase import molecule

# Create Al(111) 3-layer slab
slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)

# Adsorb an N2 molecule on the bridge site at a height of 2.0 angstroms
N2 = molecule('N2')
add_adsorbate(slab, N2, height=2.0, position='bridge')

# Print the number of atoms and atom types in the final structure
num_atoms = len(slab)
atom_types = slab.get_chemical_symbols()
print("Number of atoms:", num_atoms)
print("Atom types:", set(atom_types))
