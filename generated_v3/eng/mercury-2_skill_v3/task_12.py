from ase.build import bulk

a = 2.95
c = a * 1.59
atoms = bulk('Ti', 'hcp', a=a, c=c, cubic=False)

print("Cell vectors (Å):")
print(atoms.get_cell())
print("\nAtomic positions (Å):")
print(atoms.get_positions())
