from ase.build import fcc111, molecule, add_adsorbate
slab = fcc111('Pt', size=(1,1,4), vacuum=10.0)
add_adsorbate(slab, molecule('CO'), height=1.8, position='ontop')
print(len(slab))
