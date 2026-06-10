from ase.build import bulk, molecule, add_adsorbate, Slab

pt_bulk = bulk('Pt', 'fcc', a=3.9231)
slab = Slab(pt_bulk, (111), layers=4, vacuum=10.0)
add_adsorbate(slab, molecule('CO'), height=1.8, position=(0.5, 0.5))
print(len(slab))
