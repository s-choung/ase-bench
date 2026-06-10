from ase.build import bulk, surface

atoms = bulk('Cu', 'fcc', a=3.6)
slab = surface(atoms, indices=(2,1,1), layers=3)
slab.center(axis=2, vacuum=10)
print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
