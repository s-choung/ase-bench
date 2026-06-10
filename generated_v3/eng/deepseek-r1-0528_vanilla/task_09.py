from ase import Atoms
from ase.build import bulk
from ase.io import write, read

cu = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', cu, format='vasp')
system = read('POSCAR')
print(f"Atoms: {len(system)}, Cell: {system.cell.cellpar()}")
