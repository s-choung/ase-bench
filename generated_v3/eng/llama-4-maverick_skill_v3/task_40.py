from ase import Atoms
from ase.spacegroup import crystal
from ase.io import write, read

nacl = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])
write('nacl.cif', nacl)
nacl_read = read('nacl.cif')

print(f'Spacegroup: {nacl_read.info["spacegroup"]} ({nacl_read.info["spacegroup_symbol"]})')
print(f'Number of atoms: {len(nacl_read)}')
