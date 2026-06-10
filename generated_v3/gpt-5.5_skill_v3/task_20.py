from ase.build import nanotube

cnt = nanotube(6, 6, length=4, bond=1.42, symbol="C", vacuum=10.0)

print("Number of atoms:", len(cnt))
print("Cell:")
print(cnt.cell)
print("Cell lengths and angles [a, b, c, alpha, beta, gamma]:")
print(cnt.get_cell_lengths_and_angles())
