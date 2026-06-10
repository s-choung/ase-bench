from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)

# Write to VASP POSCAR
write('POSCAR', atoms, format='vasp')

# Read back
atoms2 = read('POSCAR')

print('Number of atoms:', len(atoms2))
print('Cell parameters (Å):')
print(atoms2.get_cell())
