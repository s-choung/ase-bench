from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

atoms = bulk('NaCl')
write('nacl.cif', atoms, format='cif')
atoms_read = read('nacl.cif', format='cif')
sg = get_spacegroup(atoms_read)
print(f'Spacegroup: {sg.symbol} (No. {sg.no})')
print(f'Number of atoms: {len(atoms_read)}')
