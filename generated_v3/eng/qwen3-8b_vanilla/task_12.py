from ase import space

a = 2.95
c_over_a = 1.59
c = a * c_over_a

atoms = space.Bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors:")
print(atoms.get_cell())
print("\nAtomic positions:")
print(atoms.get_positions())
