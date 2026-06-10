from ase.spacegroup import crystal
from ase.io import write, read

atoms = crystal(
    symbols=['Na', 'Cl'],
    basis=[(0, 0, 0), (0.5, 0, 0)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90]
)

write('nacl.cif', atoms, format='cif')

atoms_read = read('nacl.cif', format='cif')

from ase.spacegroup import get_spacegroup
sg = get_spacegroup(atoms_read)

print(f"Spacegroup: {sg}")
print(f"Spacegroup number: {sg.no}")
print(f"Spacegroup symbol: {sg.symbol}")
print(f"Number of atoms: {len(atoms_read)}")
print(f"Chemical formula: {atoms_read.get_chemical_formula()}")
