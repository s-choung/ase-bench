from ase.build import nanotube

cnt = nanotube(6, 6, length=4, symbol="C")

print("Number of atoms:", len(cnt))
print("Cell:")
print(cnt.cell)
print("Cell parameters [a, b, c, alpha, beta, gamma]:")
print(cnt.cell.cellpar())
