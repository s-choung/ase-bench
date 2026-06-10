from ase.spacegroup import crystal
from ase.io import write, read
from ase.spacegroup import get_spacegroup

atoms = crystal('NaCl', basis=[(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])
write('nacl.cif', atoms, format='cif')

atoms2 = read('nacl.cif')
sg = get_spacegroup(atoms2)

print(sg)
print(len(atoms2))
