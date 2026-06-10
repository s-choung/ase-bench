from ase.build import bulk
from ase.io import read, write
from ase.calculators.emt import EMT

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
write('POSCAR', cu, format='vasp')

cu_read = read('POSCAR', format='vasp')
print(f"Number of atoms: {len(cu_read)}")
print(f"Cell parameters (Ang): {cu_read.cell.lengths()}")
print(f"Cell angles (deg): {cu_read.cell.angles()}")
