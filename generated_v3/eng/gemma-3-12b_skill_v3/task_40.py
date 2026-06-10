from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.io import write, read
from ase.spacegroup import crystal

# Create an NaCl structure
slab = fcc111('Na', size=(2, 2, 4), vacuum=10.0)
slab += fcc111('Cl', size=(2, 2, 4), vacuum=10.0)

# Add a calculator
slab.calc = EMT()

# Write to CIF file
write('nacl.cif', slab, format='cif')

# Read back from the CIF file
atoms = read('nacl.cif')

# Print spacegroup information
print(f"Spacegroup: {atoms.spacegroup}")

# Print number of atoms
print(f"Number of atoms: {len(atoms)}")
