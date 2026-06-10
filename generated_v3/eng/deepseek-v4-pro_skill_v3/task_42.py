from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('bulk_metals.db')
for metal in ['Cu', 'Ag', 'Au']:
    atoms = bulk(metal, 'fcc', a=3.6)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, name=metal, energy=energy)

for row in db.select():
    print(f"{row.formula}: {row.energy:.6f} eV")
