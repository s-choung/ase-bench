from ase.io import read, write
from ase.build import bulk

# Create Cu FCC bulk structure
cu_fcc = bulk('Cu', 'fcc', a=3.615)

# Write Cu FCC bulk to VASP POSCAR file
write('Cu_FCC_POSCAR.vasp', cu_fcc)

# Read the Cu FCC bulk back from the VASP POSCAR file
atoms_read = read('Cu_FCC_POSCAR.vasp')

# Print the number of atoms and cell parameters
print(f"Number of atoms: {atoms_read.num_atoms}")
print(f"Cell parameters (Å): {atoms_read.cell}")
