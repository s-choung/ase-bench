from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# Create and populate database
with connect('metals.db') as db:
    for metal in ['Cu', 'Ag', 'Au']:
        atoms = bulk(metal, 'fcc')
        atoms.calc = EMT()
        db.write(atoms, energy=atoms.get_potential_energy())

# Query and print entries
with connect('metals.db') as db:
    for entry in db.select():
        print(f'Formula: {entry.formula}, Energy: {entry.energy:.6f} eV')
