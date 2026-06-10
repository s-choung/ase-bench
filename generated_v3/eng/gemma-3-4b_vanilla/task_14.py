from ase.build import fcc111, add_adsorbate
from ase.lattice import MonkCell
from ase.calculators import EMT, LJ
from ase.io import write

# Lattice constant
a = 5.64

# Create NaCl crystal in Fm-3m spacegroup (225)
cell = fcc111('Na', a, direction='z', size=(2, 2, 2))
cell.set_celltype('fcc')

# Add Na and Cl atoms
add_adsorbate(cell, 'Cl', height=0.2, position=[0.5, 0.5, 0.5])

# Add Na
add_adsorbate(cell, 'Na', height=0.1, position=[0, 0, 0])

# Set calculator
cell.calc = EMT()
cell.calc.edofmax = 10

# Periodic Boundary Conditions
cell.set_boundary('p')
cell.set_constraint('NPar')

# Calculate LJ potential energy
cell.calc = LJ(sigma=2.0, epsilon=0.5)

# Print results
print(f"Number of atoms: {len(cell)}")
print("Chemical symbols:", cell.get_chemical_symbols())

# Write to file
write('NaCl_crystal.xyz', cell)
