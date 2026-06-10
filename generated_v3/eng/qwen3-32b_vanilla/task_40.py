from ase import Atoms
from ase.io import write, read
from ase.spacegroup import get_spacegroup

a = 5.64
atoms = Atoms(['Na', 'Cl'], [[0, 0, 0], [0.5, 0.5, 0.5]], cell=(a, a, a), pbc=True)
write('nacl.cif', atoms)
atoms_read = read('nacl.cif')
spg = get_spacegroup(atoms_read)
print(f'Spacegroup: {spg.no} ({spg.symbol}), Number of atoms: {len(atoms_read)}')
