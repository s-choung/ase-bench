from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', atoms, format='vasp')

atoms2 = read('POSCAR', format='vasp')

print(f'Number of atoms: {len(atoms2)}')
a, b, c, alpha, beta, gamma = atoms2.get_cell_lengths_and_angles()
print(f'Cell parameters: a={a:.4f}, b={b:.4f}, c={c:.4f}, alpha={alpha:.2f}, beta={beta:.2f}, gamma={gamma:.2f}')
