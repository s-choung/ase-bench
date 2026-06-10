from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import Database

db = Database('materials.db', 'w')
elements = ['Cu', 'Ag', 'Au']

for symbol in elements:
    atoms = bulk(symbol, 'fcc', a=3.6)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy:.4f}")
