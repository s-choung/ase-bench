from ase import Atoms
from ase.spacegroup import crystal

# Create NaCl crystal with spacegroup 225
a = 5.64  # lattice constant in angstrom
atoms = crystal(
    symbols=['Na', 'Cl'],  # Alternative: symbols='NaCl'
    basis=[(0.0, 0.0, 0.0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[a, a, a, 90, 90, 90],  # cubic cell
)

# Print number of atoms and chemical symbols
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
