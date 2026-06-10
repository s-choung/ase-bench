from ase.build import bulk, surface, add_vacuum

fe_bulk = bulk('Fe', 'bcc', a=2.856)
fe_surf = surface(fe_bulk, (110), size=(2,2,4))
add_vacuum(fe_surf, 10)

print(len(fe_surf))
print(fe_surf.get_cell())
