from ase.build import bulk

a = 2.95
c = a * 1.59
ti = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(ti.cell)
print("\nAtomic positions (fractional):")
print(ti.get_scaled_positions())
print("\nAtomic positions (Cartesian, Å):")
print(ti.positions)
