from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)

# Save as VASP POSCAR
write('POSCAR', cu, format='vasp')

# Read back
cu2 = read('POSCAR', format='vasp')

# Output information
print('Number of atoms:', len(cu2))
print('Cell parameters (Å):')
print(cu2.get_cell())
