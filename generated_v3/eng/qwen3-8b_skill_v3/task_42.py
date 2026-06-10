from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

db = connect('bulk_energies.db')
metals = ['Cu', 'Ag', 'Au']
for s in metals:
    atoms = bulk(s, 'fcc')
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    db.write(atoms, formula=s, energy=e)
for entry in db.select():
    print(f"Formula: {entry.formula}, Energy: {entry.energy}")
