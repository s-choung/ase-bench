from ase.build import bulk

# Create Cu FCC bulk with lattice constant 3.6
atoms = bulk('Cu', 'fcc', a=3.6)

# Generate a 2x2x2 supercell
supercell = atoms.repeat((2, 2, 2))

# Print cell info (lengths and angles) and number of atoms
print(f"Cell lengths and angles: {supercell.get_cell_lengths_and_angles()}")
print(f"Number of atoms: {len(supercell)}")
