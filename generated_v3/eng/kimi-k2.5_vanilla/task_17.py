from ase.build import surface

slab = surface('Cu', (2, 1, 1), layers=3, vacuum=10.0)

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.cell}")
