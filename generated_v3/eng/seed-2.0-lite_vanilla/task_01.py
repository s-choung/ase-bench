from ase.build import bulk

# Create FCC bulk Cu with experimental lattice constant
cu_fcc = bulk('Cu', 'fcc', a=3.615)
# Generate 2x2x2 supercell
supercell = cu_fcc.repeat((2, 2, 2))

# Output required information
print("Supercell lattice vectors (Å):\n", supercell.cell)
print("Total number of atoms:", len(supercell))
