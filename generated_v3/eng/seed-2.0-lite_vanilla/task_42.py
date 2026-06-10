from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create and populate database
with connect('noble_metals.db') as db:
    for symbol in ['Cu', 'Ag', 'Au']:
        atoms = bulk(symbol, 'fcc')
        atoms.calc = EMT()
        db.write(atoms)

    # Query all entries and print results
    for row in db.select():
        print(f"Formula: {row.formula:2s} | Total Energy: {row.energy:.3f} eV")
