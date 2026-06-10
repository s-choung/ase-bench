from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Pt', size=(2, 2, 4), a=3.92, vacuum=10)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

print(len(slab))
