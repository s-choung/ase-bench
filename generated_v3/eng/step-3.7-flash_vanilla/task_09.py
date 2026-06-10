from ase.build import bulk
from ase.io import read, write

cu = bulk('Cu', 'fcc', a=3.61)
write('POSCAR', cu, format='vasp')
cu_loaded = read('POSCAR', format='vasp')
print(f"Number of atoms: {len(cu_loaded)}")
print(f"Cell parameters (Å):\n{cu_loaded.cell}")
