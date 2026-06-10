from ase.build import bulk
from ase.io import read, write

atoms = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', atoms, format='vasp')

loaded_atoms = read('POSCAR', format='vasp')

print(f"Number of atoms: {len(loaded_atoms)}")
print(f"Cell parameters:\n{loaded_atoms.get_cell()}")
