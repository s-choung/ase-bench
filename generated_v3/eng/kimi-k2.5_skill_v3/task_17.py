from ase.build import bulk, surface

cu = bulk('Cu', 'fcc', a=3.61)
slab = surface(cu, (2, 1, 1), layers=3, vacuum=10)

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.cell}")
