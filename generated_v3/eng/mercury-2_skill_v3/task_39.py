from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Build FCC Au bulk
au = bulk('Au', 'fcc', a=4.08, cubic=True)
# Save to XYZ
write('au_bulk.xyz', au)

# Read back
au2 = read('au_bulk.xyz')

# Print element symbols and Cartesian positions
for sym, pos in zip(au2.get_chemical_symbols(), au2.get_positions()):
    print(f'{sym}  {pos[0]: .6f}  {pos[1]: .6f}  {pos[2]: .6f}')
