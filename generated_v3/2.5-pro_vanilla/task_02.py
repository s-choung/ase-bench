```python
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Pt(111) 4층 slab 생성 (2x2 surface cell)
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0, orthogonal=True)

# CO 분자 생성 (C-O bond length ~1.15 Angstrom)
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.15)])

# ontop 사이트에 CO 흡착 (Pt-C height ~1.85 Angstrom)
add_adsorbate(slab, co, 1.85
