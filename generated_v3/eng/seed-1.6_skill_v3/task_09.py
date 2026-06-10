from ase.build import bulk
from ase.io import read, write

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)
# Save to VASP POSCAR
write('POSCAR', cu_bulk, format='vasp')
# Read back POSCAR
cu_read = read('POSCAR', format='vasp')
# Print required properties
print(f'Number of atoms: {cu_read.get_global_number_of_atoms()}')
print(f'Cell parameters (a, b, c, α, β, γ): {cu_read.get_cell_lengths_and_angles()}')
