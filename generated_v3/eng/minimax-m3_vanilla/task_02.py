from ase.build import fcc111, molecule

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
slab.add_adsorbate(co, height=1.85, position='ontop')

print(f"Number of atoms: {len(slab)}")
