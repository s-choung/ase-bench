from ase.build import fcc111, add_adsorbate

slab = fcc111('Pt', (2, 2, 4), vacuum=10.0)
co = Atoms('CO', positions=[[0, 0, -0.564], [0, 0, 0.564]])
add_adsorbate(slab, co, 2.0, (0, 0))
print(len(slab))
