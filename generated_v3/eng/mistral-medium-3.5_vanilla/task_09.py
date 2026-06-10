from ase.lattice.cubic import FaceCenteredCubic
from ase.io import write, read

# Create Cu FCC bulk
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                          symbol="Cu",
                          size=(1, 1, 1),
                          pbc=True)

# Save to POSCAR
write('POSCAR', atoms, format='vasp')

# Read from POSCAR
atoms_read = read('POSCAR', format='vasp')

# Print details
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters: {atoms_read.cell}")
