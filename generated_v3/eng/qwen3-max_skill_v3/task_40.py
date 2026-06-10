from ase import Atoms
from ase.io import read, write
from ase.spacegroup import get_spacegroup

# Create NaCl crystal (rock salt structure)
a = 5.64  # lattice constant in Angstrom
nacl = Atoms(
    symbols=['Na', 'Cl'],
    positions=[[0, 0, 0], [0.5*a, 0.5*a, 0.5*a]],
    cell=[a, a, a],
    pbc=True
)

# Save to CIF
write('NaCl.cif', nacl, format='cif')

# Read back from CIF
nacl_read = read('NaCl.cif', format='cif')

# Print spacegroup and number of atoms
print(f"Spacegroup: {get_spacegroup(nacl_read)}")
print(f"Number of atoms: {len(nacl_read)}")
