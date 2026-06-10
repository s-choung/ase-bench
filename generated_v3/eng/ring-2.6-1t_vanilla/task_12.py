from ase.build import bulk

a = 2.95
c_over_a = 1.59
c = a * c_over_a

atoms = bulk('Ti', crystalstructure='hcp', a=a, c=c)

print("Cell vectors:")
print(atoms.cell)
print("\nAtomic positions (Cartesian):")
print(atoms.positions)
