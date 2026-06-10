from ase.build import bulk
from ase.io import read, write

atoms = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', atoms, format='vasp')
atoms_read = read('POSCAR', format='vasp')

print(f"Number of atoms: {len(atoms_read)}")
params = atoms_read.get_cell_lengths_and_angles()
print(f"Cell: a={params[0]:.2f}, b={params[1]:.2f}, c={params[2]:.2f}, "
      f"α={params[3]:.1f}, β={params[4]:.1f}, γ={params[5]:.1f}")
