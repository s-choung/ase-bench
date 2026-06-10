from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {sorted(set(slab.get_chemical_symbols()))}")
