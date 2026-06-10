from ase import Atoms
from ase.build import fcc111, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT
from ase.io import write

# Create Al(111) 3-layer slab
slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)

# Create N2 molecule
co = molecule('N2')

# Add N2 molecule to the slab at the bridge site
add_adsorbate(slab, co, height=2.0, position='bridge')

# Add vacuum
add_vacuum(slab, 10.0)

# Get the number of atoms and atom types
num_atoms = len(slab)
atom_types = [atom.symbol for atom in slab]

# Print the results
print("Number of atoms:", num_atoms)
print("Atom types:", atom_types)

# Write the final structure to a POSCAR file
write('AlN2_slab.poscar', slab, format='vasp')
