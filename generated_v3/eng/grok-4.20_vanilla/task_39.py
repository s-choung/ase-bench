from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.078, cubic=True)

# Write to XYZ
write('au_bulk.xyz', atoms)

# Read back
atoms2 = read('au_bulk.xyz')

# Print
print(atoms2.get_chemical_symbols())
print(atoms2.get_positions())
