"""T3 Vanilla: Pt(111) surface with CO adsorbate"""
from ase.build import fcc111, add_adsorbate

slab = fcc111('Pt', size=(2, 2, 3), vacuum=7.0)
add_adsorbate(slab, 'CO', 1.8, 'ontop')
print(f"Number of atoms: {len(slab)}")
print(f"Symbols: {slab.get_chemical_symbols()}")
