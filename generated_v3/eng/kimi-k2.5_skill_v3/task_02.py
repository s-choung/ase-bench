from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Pt', size=(1, 1, 4), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
print(slab.get_number_of_atoms())
