from ase import Atoms
from ase.spacegroup import crystal

# Create NaCl crystal
nacl = crystal(['Na', 'Cl'],
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225,
               cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Print information
print(f"Number of atoms: {len(nacl)}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")
