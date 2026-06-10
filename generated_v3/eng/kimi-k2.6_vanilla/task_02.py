from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.85, position=(0, 0))
print(len(slab))
