from ase.spacegroup import crystal
from ase import Atoms

# Create NaCl structure with spacegroup 225 (Fm-3m)
a = 5.64  # lattice constant in Angstroms
atoms = crystal(['Na', 'Cl'], 
                [(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225,
                cellpar=[a, a, a, 90, 90, 90])

# Print number of atoms and chemical symbols
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
