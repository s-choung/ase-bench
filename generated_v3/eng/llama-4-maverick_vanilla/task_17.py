from ase.build import bulk, surface

cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_surface = surface(cu_bulk, (2, 1, 1), 3, vacuum=10)
print(len(cu_surface))
print(cu_surface.cell)
