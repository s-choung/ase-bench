from ase import Atoms
from ase.build import molecule, fcc111
from ase.visualize import view

# Create Al(111) 3-layer slab with 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10)

# Create N2 molecule
n2 = molecule('N2')
n2.rotate(90, 'x')  # Align horizontally for bridge site

# Place N2 at bridge site, ~2.0 Å above surface
n2.translate(slab[0].position + [1.5, 0.87, 2.0])  # Approximate bridge site

# Combine slab and N2
system = slab + n2

# Print number of atoms and atom types
print(len(system))
print(system.get_chemical_symbols())
