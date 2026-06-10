from ase import Atoms
from ase.io import write, read

# Create Au FCC structure
atoms = Atoms('Au', pbc=True, cell=[4.08, 4.08, 4.08])
atoms.set_scaled_positions([[0, 0, 0]])
atoms = atoms.repeat((2, 2, 2))

# Write to file
write('au_bulk.xyz', atoms)

# Read back from file
atoms_read = read('au_bulk.xyz')

# Print atom types and positions
print("Atom types and positions:")
for i, (symbol, pos) in enumerate(zip(atoms_read.get_chemical_symbols(), atoms_read.get_positions())):
    print(f"{i}: {symbol} {pos}")
