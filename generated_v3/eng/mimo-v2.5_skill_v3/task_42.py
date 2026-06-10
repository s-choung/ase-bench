import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create database and calculator
db = connect('metals.db')
calc = EMT()

# Build and store structures with energies
for symbol, a in [('Cu', 3.6), ('Ag', 4.09), ('Au', 4.07)]:
    atoms = bulk(symbol, 'fcc', a=a, cubic=True)
    atoms.calc = calc
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy, name=f'{symbol}_bulk')

# Query and print all entries
for row in db.select():
    print(f"{row.formula}: {row.energy:.4f} eV")
