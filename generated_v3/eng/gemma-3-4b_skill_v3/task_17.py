import numpy as np
from ase import Atoms
from ase.build import surface, add_vacuum
from ase.calculators.emt import EMT
from ase.io import write

# Create a Cu bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True, orthorhombic=True)
atoms.calc = EMT()

# Create a (2,1,1) surface
surface_atoms = surface('Cu', indices=(2, 1, 1), layers=3)
surface_atoms.calc = EMT()

# Combine the bulk and the surface
atoms = atoms + surface_atoms

# Add vacuum
add_vacuum(atoms, 10.0)

# Print the number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print the cell
print("Cell:")
print(atoms.get_cell())

# Write the structure to a POSCAR file
write('Cu_surface.poscar', atoms, format='vasp')
