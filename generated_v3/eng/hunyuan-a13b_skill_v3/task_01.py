from ase import Atoms

# Create Cu FCC bulk structure
bulk_first = Atoms('Cu', 'fcc', a=3.5668)  # Cu FCC lattice constant in Å
supercell = bulk_first.repeat((2, 2, 2))

# Print cell information and number of atoms
print("Supercell cell parameters (Å):")
print(supercell.frame_cell())  # 3x3 cell vectors (a, b, c)
print("
Number of atoms:", len(supercell))
