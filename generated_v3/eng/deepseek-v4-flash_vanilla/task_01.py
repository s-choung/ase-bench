from ase.build import bulk

# Create Cu fcc bulk and 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.615)
supercell = atoms * (2, 2, 2)

# Print cell info and number of atoms
print("Cell parameters (Å):", supercell.cell.lengths())
print("Angles (deg):", supercell.cell.angles())
print("Number of atoms:", len(supercell))
