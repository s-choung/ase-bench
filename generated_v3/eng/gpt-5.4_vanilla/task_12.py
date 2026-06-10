from ase.build import bulk

a = 2.95
c_over_a = 1.59
atoms = bulk('Ti', 'hcp', a=a, c=a * c_over_a)

print("Cell vectors (Angstrom):")
for v in atoms.cell:
    print(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}")

print("\nAtomic positions (Angstrom):")
for i, pos in enumerate(atoms.positions):
    print(f"{i:2d} {atoms[i].symbol}  {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}")
