from ase.build import bulk
from ase.io import read, write

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Save as POSCAR
write('POSCAR', cu_bulk, format='vasp')

# Read back POSCAR
atoms = read('POSCAR')

# Print information
print(f"Number of atoms: {len(atoms)}")
print("Cell parameters:")
print(atoms.get_cell())
