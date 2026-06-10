from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)

# Save as POSCAR
write('POSCAR', atoms, format='vasp')

# Read back
atoms_read = read('POSCAR', format='vasp')

# Print info
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters (a, b, c, α, β, γ): {atoms_read.get_cell_lengths_and_angles()}")
