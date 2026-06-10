from ase.build import bulk
from ase.io import read, write

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
write('POSCAR', atoms, format='vasp')

atoms_read = read('POSCAR', format='vasp')
print("Number of atoms:", len(atoms_read))
a, b, c, alpha, beta, gamma = atoms_read.get_cell_lengths_and_angles()
print(f"a={a:.4f} b={b:.4f} c={c:.4f} Å")
print(f"alpha={alpha:.2f} beta={beta:.2f} gamma={gamma:.2f} deg")
