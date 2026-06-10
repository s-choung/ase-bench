from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', atoms, format='vasp')

atoms_read = read('POSCAR', format='vasp')
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters (a, b, c, α, β, γ): {atoms_read.get_cell_lengths_and_angles()}")
