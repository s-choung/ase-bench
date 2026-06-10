from ase import Atoms
from ase.build import bulk
from ase.io import write, read

cu = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', cu, format='vasp')
read_cu = read('POSCAR', format='vasp')
print(f"Atoms: {len(read_cu)}")
print(f"Cell: {read_cu.cell.lengths()[:3]} {read_cu.cell.angles()[:3]}")
