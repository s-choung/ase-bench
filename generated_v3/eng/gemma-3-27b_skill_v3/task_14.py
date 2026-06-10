from ase import Atoms
from ase.spacegroup import crystal
from ase.visualize import view

a = 5.64
atoms = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225,
                cell=[a, a, a],
                symbol='Na', symbol2='Cl')

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")

# view(atoms) # Optional: Visualize the structure
