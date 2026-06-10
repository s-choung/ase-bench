from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Write to POSCAR
write('POSCAR', atoms, format='vasp')

# Read from POSCAR
atoms_read = read('POSCAR', format='vasp')

# Print number of atoms and cell parameters
print(f"Number of atoms: {len(atoms_read)}")
a, b, c, alpha, beta, gamma = atoms_read.get_cell_lengths_and_angles()
print(f"Cell parameters: a={a:.2f} Å, b={b:.2f} Å, c={c:.2f} Å, "
      f"α={alpha:.2f}°, β={beta:.2f}°, γ={gamma:.2f}°")
