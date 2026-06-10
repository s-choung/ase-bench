from ase import Atoms
from ase.build import nanotube
from ase.io import write

# Create a (6,6) carbon nanotube with length=4
cnt = nanotube(6, 6, length=4)

# Print the number of atoms and cell info
print(f'Number of atoms: {len(cnt)}')
print('Cell info:')
print(cnt.get_cell_lengths_and_angles())

# Optionally, write to a file for further analysis or visualization
write('cnt.xyz', cnt)
