from ase.build import bcc110
from ase import units

# Create an Fe BCC(110) surface
size = (2, 2, 4)
vacuum = 10  # angstroms

atoms = bcc110('Fe', size=size, vacuum=vacuum)

# Print the number of atoms
print(f'Number of atoms: {len(atoms)}')

# Print the cell size
cell = atoms.get_cell_lengths_and_angles()
print(f'Cell size: \na={cell[0]} Å, b={cell[1]} Å, c={cell[2]} Å')
print(f'Cell angles: α={cell[3]}°, β={cell[4]}°, γ={cell[5]}°')
