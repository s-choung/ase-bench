from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(3, 3, layers), a=3.61, vacuum=10.0)
    slab.calc = EMT()
    energy = slab.get_potential_energy()
    db.write(slab, layers=layers, energy=energy)

rows = db.select('layers=3')
for row in rows:
    atoms = row.toatoms()
    print(f"Layers: {row.layers}, Number of atoms: {len(atoms)}")
