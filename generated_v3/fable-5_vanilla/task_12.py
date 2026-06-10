from ase.build import bulk

a = 2.95
c = a * 1.59

ti = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(ti.get_cell())
print("Atomic positions:")
print(ti.get_positions())
