from ase.spacegroup import crystal, get_spacegroup
from ase.io import write, read

atoms = crystal(['Na', 'Cl'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225,
                cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

write('NaCl.cif', atoms)
atoms2 = read('NaCl.cif')

sg = get_spacegroup(atoms2)
print(sg.no, sg.symbol)
print(len(atoms2))
