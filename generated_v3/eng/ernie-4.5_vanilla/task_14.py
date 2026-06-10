from ase import Atoms
from ase.spacegroup import crystal

# Create an NaCl crystal using space group 225 (Fm-3m)
a = 5.64  # Lattice constant in angstroms
atoms = crystal(
    symbols=['Na', 'Cl'],  # Chemical symbols
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],  # Positions of Na and Cl
    spacegroup=225,  # Space group Fm-3m
    cellparam=[a, a, a, 90, 90, 90],  # Cell parameters
    primitive_cell=True
)

# Print the number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print the chemical symbols
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
