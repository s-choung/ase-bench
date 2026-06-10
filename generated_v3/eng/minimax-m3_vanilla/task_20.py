from ase.build import nanotube

cnt = nanotube(6, 6, length=4, bond=1.42, symbol='C')

print(f"Number of atoms: {len(cnt)}")
print("Cell:")
print(cnt.cell)
print("Periodic boundary conditions:", cnt.pbc)
