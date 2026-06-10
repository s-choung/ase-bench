from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.6)
write('Cu_POSCAR.vasp', atoms, format='vasp')

loaded = read('Cu_POSCAR.vasp', format='vasp')
n_atoms = len(loaded)
a, b, c, alpha, beta, gamma = loaded.get_cell_lengths_and_angles()

print(f"Number of atoms: {n_atoms}")
print(f"Cell parameters:")
print(f"  a = {a:.4f} Å")
print(f"  b = {b:.4f} Å")
print(f"  c = {c:.4f} Å")
print(f"  α = {alpha:.2f}°")
print(f"  β = {beta:.2f}°")
print(f"  γ = {gamma:.2f}°")
