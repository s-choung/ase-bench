from ase import Atoms
from ase.io import write, read

cu_fcc = Atoms('Cu',
               cell=[(0, 0.5, 0.5),
                     (0.5, 0, 0.5),
                     (0.5, 0.5, 0)],
               pbc=True)

write('Cu_fcc.vasp', cu_fcc)

cu_fcc_read = read('Cu_fcc.vasp')

print("Number of atoms:", len(cu_fcc_read))
print("Cell parameters:", cu_fcc_read.cell)
