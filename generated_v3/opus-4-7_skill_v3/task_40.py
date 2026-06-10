from ase.spacegroup import crystal
from ase.io import read, write

nacl = crystal(['Na', 'Cl'], basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

write('nacl.cif', nacl)
atoms = read('nacl.cif')

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical formula: {atoms.get_chemical_formula()}")
print(f"Cell parameters: {atoms.cell.cellpar()}")

if 'spacegroup' in atoms.info:
    print(f"Spacegroup: {atoms.info['spacegroup']}")
else:
    from ase.spacegroup import get_spacegroup
    sg = get_spacegroup(atoms)
    print(f"Spacegroup: {sg}")
