```python
from ase import Atoms
from ase.io import write, read

atoms = Atoms('Cu', positions=[[0, 0, 0]], cell=[[0, 1, 1], [1,; 0, 1], [1, 1, 0]], pbc=True)
write('POSCAR', atoms, format='vasp')
atoms_read = read('POSCAR', format='vasp')
print(len(atoms_read))
print(atoms_read.get_cell())
