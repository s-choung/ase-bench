from ase.build import bulk, surface

cu_bulk = bulk('Cu', 'fcc', a=3.61)
cu_surf = surface(cu_bulk, (2, 1, 1), layers=3, vacuum=10.0)

print("Number of atoms:", len(cu_surf))
print("Cell:\n", cu_surf.cell[:])
