from ase.build import bulk

a = 2.95
c = 1.59 * a

ti = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors (rows):")
print(ti.cell)
print("\nAtomic positions (cartesian):")
print(ti.positions)
