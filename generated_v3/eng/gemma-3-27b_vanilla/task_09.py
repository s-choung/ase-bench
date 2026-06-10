from ase.build import fcc111
from ase.io import write, read
from ase.lattice.cubic import Cubic

cu = fcc111('Cu', size=(2, 2, 2))
write('Cu_FCC.poscar', cu, format='vasp')
cu_read = read('Cu_FCC.poscar', format='vasp')

print(f"Number of atoms: {len(cu_read.get_atoms())}")
print(f"Cell parameters (Angstrom):")
print(cu_read.get_cell())
