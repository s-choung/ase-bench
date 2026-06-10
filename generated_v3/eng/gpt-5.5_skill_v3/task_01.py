from ase.build import bulk

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)
supercell = atoms * (2, 2, 2)

print("Cell:")
print(supercell.cell)
print("Cell lengths and angles [a, b, c, alpha, beta, gamma]:")
print(supercell.get_cell_lengths_and_angles())
print("Number of atoms:", len(supercell))
