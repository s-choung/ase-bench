from ase.build import bulk

# Create Cu FCC bulk and 2x2x2 supercell
cu_bulk = bulk('Cu', 'fcc')
supercell = cu_bulk.repeat((2, 2, 2))

# Print cell info and number of atoms
print("Supercell cell (Å):\n", supercell.cell)
la = supercell.get_cell_lengths_and_angles()
print(f"Lengths (Å): {la[:3]}, Angles (deg): {la[3:]}")
print(f"Number of atoms: {len(supercell)}")
