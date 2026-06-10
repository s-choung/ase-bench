from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

atoms = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)
write('NaCl.cif', atoms)
atoms_read = read('NaCl.cif')
sg = get_spacegroup(atoms_read)
print(f"Space group: {sg.symbol} ({sg.number})")
print(f"Number of atoms: {len(atoms_read)}")
