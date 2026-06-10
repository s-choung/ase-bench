from ase.build import bulk
from ase.io import read, write

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
write('POSCAR', atoms, format='vasp')

atoms_read = read('POSCAR', format='vasp')
print(f"원자 수: {len(atoms_read)}")
cell_params = atoms_read.get_cell_lengths_and_angles()
print(f"a={cell_params[0]:.4f}, b={cell_params[1]:.4f}, c={cell_params[2]:.4f} Å")
print(f"α={cell_params[3]:.2f}°, β={cell_params[4]:.2f}°, γ={cell_params[5]:.2f}°")
