from ase.build import bulk, surface, add_vacuum

atoms_bulk = bulk('Cu', 'fcc', a=3.61)
atoms_surface = surface(atoms_bulk, (2,1,1), layers=3)
add_vacuum(atoms_surface, 10)
print("Atoms:", len(atoms_surface))
print("Cell:", atoms_surface.get_cell())
