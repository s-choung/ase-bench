from ase.build import bulk

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.615)

# Generate 2x2x2 supercell
supercell = cu.repeat((2, 2, 2))

# Print cell info and number of atoms
print("Cell:\n", supercell.cell)
print("Number of atoms:", len(supercell))
print("Cell parameters:", supercell.cell.cellpar())
