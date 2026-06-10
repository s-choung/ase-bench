from ase import Atoms
from ase.spacegroup import crystal
from ase.io import write, read

atoms = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, cubic=True)
write('nacl.cif', atoms)

read_atoms = read('nacl.cif')[0]
print(read_atoms.get_space_group_name())
print(len(read_atoms))
