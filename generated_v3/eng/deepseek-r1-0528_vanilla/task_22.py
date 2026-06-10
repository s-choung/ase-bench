from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position=(0.25, 0.25))

print(f"Number of atoms: {len(slab)}")
symbols = set(slab.get_chemical_symbols())
print(f"Atom types: {', '.join(symbols)}")
