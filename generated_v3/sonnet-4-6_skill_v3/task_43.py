from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_slabs.db')

for n in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, n), vacuum=10.0)
    slab.calc = EMT()
    slab.get_potential_energy()
    db.write(slab, layers=n)

for row in db.select(layers=3):
    atoms = row.toatoms()
    print(f"layers=3 구조 원자 수: {len(atoms)}")
