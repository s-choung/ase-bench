from ase import Atoms
from ase.io import read, write
from ase.spacegroup import get_spacegroup

a = 5.64
atoms = Atoms('Na4Cl4',
              cell=[[a, 0, 0], [0, a, 0], [0, 0, a]],
              scaled_positions=[[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5],
                                [0, 0.5, 0.5], [0.5, 0, 0], [0, 0.5, 0],
                                [0, 0, 0.5], [0.5, 0.5, 0.5]],
              pbc=True)

write('nacl.cif', atoms)
atoms2 = read('nacl.cif')

sg = get_spacegroup(atoms2)
print(f'Spacegroup: {sg}')
print(f'Number of atoms: {len(atoms2)}')
