"""T3 Wiki: Pt(111) surface with CO adsorbate"""
from ase import Atoms
from ase.build import fcc111, add_adsorbate

slab = fcc111('Pt', size=(2, 2, 3), vacuum=7.0)
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.16)])
add_adsorbate(slab, co, 1.8, 'ontop')
print(f"Number of atoms: {len(slab)}")
print(f"Symbols: {slab.get_chemical_symbols()}")
print(f"PBC: {slab.get_pbc()}")
