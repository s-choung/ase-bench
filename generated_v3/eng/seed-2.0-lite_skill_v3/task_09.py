from ase.build import bulk
from ase.io import read, write

# Create FCC Cu bulk
cu_bulk = bulk('Cu', 'fcc', a=3.615, cubic=True)
# Save to VASP POSCAR format
write('POSCAR', cu_bulk, format='vasp')
# Read back the saved POSCAR
read_cu = read('POSCAR', format='vasp')

# Print required outputs
print(f"Number of atoms: {len(read_cu)}")
cell_params = read_cu.get_cell_lengths_and_angles()
print(f"Cell parameters (a,b,c [Å], α,β,γ [deg]): {cell_params.round(4)}")
