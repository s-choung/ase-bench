from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
# Save as VASP POSCAR
write('POSCAR', atoms, format='vasp')
# Read back
atoms2 = read('POSCAR', format='vasp')

# Output
print('Number of atoms:', len(atoms2))
print('Cell lengths and angles (Å, degrees):', atoms2.get_cell_lengths_and_angles())
