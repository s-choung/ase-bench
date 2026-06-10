from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create database and add structures
db = connect('metals.db', append=False)

for element in ['Cu', 'Ag', 'Au']:
    atoms = bulk(element, cubic=True)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy, element=element)

# Query and print results
for row in db.select():
    print(f"{row.formula}: {row.energy:.3f} eV")
