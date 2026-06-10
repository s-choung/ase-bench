from ase.io import write, read
from ase.build import fcc111
import ase.calculators.emt as emt
import ase.calculators.lj as lj

# Create NaCl structure
atoms = fcc111('Na', size=2, a=4.6)
atoms.set_scaled_positions((0.0,0.0,0.0))
atoms.set_scaled_positions(('Na', (0.0, 0.0, 0.0)))
atoms.set_scaled_positions(('Cl', (0.5, 0.5, 0.5)))

# Write to CIF
write('NaCl.cif', atoms)

# Read back
atoms2 = read('NaCl.cif')

# Print spacegroup and number of atoms
print(atoms2.cell.spacegroup)
print(len(atoms2))
