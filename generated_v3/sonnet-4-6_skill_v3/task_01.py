from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
supercell = atoms * (2, 2, 2)

print("Cell vectors:")
print(supercell.get_cell())
print("\nCell lengths and angles:", supercell.get_cell_lengths_and_angles())
print("Number of atoms:", len(supercell))
