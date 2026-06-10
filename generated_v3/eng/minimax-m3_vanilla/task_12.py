from ase.build import hcp

# Ti HCP bulk: a = 2.95 Å, c/a = 1.59
a = 2.95
c = a * 1.59  # c = 4.6905 Å

atoms = hcp(symbol='Ti', a=a, c=c)

print("Cell vectors (Angstrom):")
print(atoms.cell.array)

print("\nAtomic positions (Cartesian, Angstrom):")
print(atoms.positions)
