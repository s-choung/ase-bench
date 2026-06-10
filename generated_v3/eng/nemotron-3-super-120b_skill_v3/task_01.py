from ase.build import bulk

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Generate 2x2x2 supercell
supercell = cu_bulk * (2, 2, 2)

# Print cell information and number of atoms
print("Cell lengths and angles (a,b,c,α,β,γ):", supercell.get_cell_lengths_and_angles())
print("Number of atoms:", len(supercell))
