from ase.build import bulk
from ase.io import read, write

cu = bulk('Cu', 'fcc')
write('POSCAR', cu, format='vasp')

atoms = read('POSCAR', format='vasp')
print(f"Number of atoms: {len(atoms)}")
print(f"Cell parameters [a, b, c, α, β, γ]: {atoms.get_cell_lengths_and_angles()}")
