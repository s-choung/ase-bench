from ase.spacegroup import crystal
from ase.io import write, read
from ase.spacegroup import get_spacegroup

nacl = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

write('nacl.cif', nacl)

atoms = read('nacl.cif')
sg = get_spacegroup(atoms)

print('Spacegroup:', sg.symbol, sg.no)
print('Number of atoms:', len(atoms))
