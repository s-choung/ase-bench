from ase import Atoms
from ase.io import read, write
from ase.spacegroup import get_spacegroup, crystal

# Build NaCl crystal (rock salt, spacegroup 225, lattice constant 5.64 Å)
atoms = crystal(['Na', 'Cl'],
                basis=[(0, 0, 0), (0.5, 0, 0)],
                spacegroup=225,
                cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Save in CIF format
write('nacl.cif', atoms, format='cif')

# Read back
atoms_read = read('nacl.cif', format='cif')

# Print spacegroup information
sg = get_spacegroup(atoms_read, symprec=1e-3)
print(f"Spacegroup: {sg.symbol} (no. {sg.no})")
print(f"Number of atoms: {len(atoms_read)}")
