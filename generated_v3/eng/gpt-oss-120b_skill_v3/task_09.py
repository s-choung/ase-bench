from ase.build import bulk
from ase.io import write, read

# Build Cu FCC bulk (lattice constant ~3.6 Å)
atoms = bulk('Cu', 'fcc', a=3.6)

# Save as VASP POSCAR
write('POSCAR', atoms, format='vasp')

# Read it back
atoms_read = read('POSCAR', format='vasp')

# Output number of atoms and cell parameters (a, b, c, α, β, γ)
print('Number of atoms:', len(atoms_read))
print('Cell lengths & angles (Å, degrees):',
      *atoms_read.get_cell_lengths_and_angles())
