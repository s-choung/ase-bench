from ase.build import bulk, surface

cu_bulk = bulk('Cu', 'fcc')
cu_surface = surface(cu_bulk, (2,1,1), layers=3, vacuum=10.0)

print(len(cu_surface))
print(cu_surface.cell)
