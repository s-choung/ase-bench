from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import write, read

# Create Au FCC bulk structure
atoms = bulk('Au', 'fcc', a=4.08)

# Save to XYZ file
write('au_fcc.xyz', atoms)

# Read back the XYZ file
atoms_read = read('au_fcc.xyz')

# Print atom symbols and positions
for sym, pos in zip(atoms_read.get_chemical_symbols(), atoms_read.get_positions()):
    print(sym, pos)
