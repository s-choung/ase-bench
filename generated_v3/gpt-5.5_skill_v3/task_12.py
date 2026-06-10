from ase.build import bulk

atoms = bulk("Ti", "hcp", a=2.95, covera=1.59)

print("Cell vectors:")
print(atoms.get_cell())

print("Atomic positions:")
print(atoms.get_positions())
