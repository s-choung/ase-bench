from ase.build import bulk, make_supercell

# Create Cu FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Create 2x2x2 supercell
supercell_matrix = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
cu_supercell = make_supercell(cu_bulk, supercell_matrix)

# Print cell info and number of atoms
print('Cell info:', cu_supercell.get_cell())
print('Number of atoms:', len(cu_supercell))
