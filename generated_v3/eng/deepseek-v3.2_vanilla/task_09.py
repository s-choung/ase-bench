from ase import Atoms
from ase.io import read, write
import numpy as np

# Create Cu FCC bulk
cu = Atoms('Cu', cell=np.eye(3) * 3.61, pbc=True)
cu = cu.repeat((3, 3, [?]))

# Save as POSCAR
write('POSCAR', cu, format='vasp', vasp5=True)

# Read back
cu_from_file = read('POSCAR', format='vasp')

# Print info
print(f'Atoms: {len(cu_from_file)}')
print(f'Cell parameters:\n{cu_from_file.cell}')
