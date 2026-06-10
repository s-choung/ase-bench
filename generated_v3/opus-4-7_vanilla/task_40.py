from ase.spacegroup import crystal
from ase.io import write, read
from ase.spacegroup import get_spacegroup

a = 5.64
nacl = crystal(['Na', 'Cl'], basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225, cellpar=[a, a, a, 90, 90, 90])

write('nacl.cif', nacl)
atoms = read('nacl.cif')

sg = get_spacegroup(atoms)
print(f"Spacegroup: {sg.symbol} (No. {sg.no})")
print(f"Number of atoms: {len(atoms)}")
