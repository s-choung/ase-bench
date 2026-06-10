from ase import Atoms
from ase.spacegroup import crystal

# Create NaCl crystal structure with spacegroup 225 (Fm-3m)
atoms = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cellpar=5.64)

# Print number of atoms and chemical symbols
print("Number of atoms:", len(atoms))
print("Chemical symbols:", atoms.get_chemical_symbols())
