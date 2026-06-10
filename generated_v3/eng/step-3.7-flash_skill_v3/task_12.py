from ase.build import bulk

a = 2.95
c = a * 1.59
ti_hcp = bulk('Ti', 'hcp', a=a, c=c)

print("Unit cell vectors (Å):")
print(ti_hcp.cell)
print("\nAtomic positions (Å):")
print(ti_hcp.get_positions())
