from ase.build import fcc111, add_adsorbate, molecule

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

symbols = slab.get_chemical_symbols()
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {sorted(set(symbols))}")
for s in sorted(set(symbols)):
    print(f"  {s}: {symbols.count(s)}")
