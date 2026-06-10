from ase.build import bulk

a = 2.95
c_over_a = 1.59
c = a * c_over_a

ti = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(ti.cell)
print("\nAtomic positions:")
print(ti.positions)
