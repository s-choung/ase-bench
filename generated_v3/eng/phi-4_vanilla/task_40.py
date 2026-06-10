from ase import Atoms
from ase.io import write, read
from ase.spacegroup import crystal
from ase.data import atomic_numbers

# Define NaCl crystal structure
def create_nacl_crystal(cell=(3, 3, 3), symbols=('Na', 'Cl')):
    lattice = crystal(chemical_formula='NaCl', primitive=True)
    for i, symbol in enumerate(symbols):
        positions = [(i%2, i//2, i//2)]
        lattice.translate(lattice[i, :] + positions[i], to_unit_cell=True)
        lattice[i].symbol = symbol
        lattice[i].number = atomic_numbers[symbol]
    return lattice

# Create NaCl crystal structure
atoms = create_nacl_crystal([3, 3, 3], ('Na', 'Cl'))

# Write to CIF
write('nacl.cif', atoms)

# Read from CIF
atoms_read = read('nacl.cif')

# Print spacegroup and number of atoms
print("Spacegroup:", atoms_read.get_space_group())
print("Number of atoms:", len(atoms_read))
