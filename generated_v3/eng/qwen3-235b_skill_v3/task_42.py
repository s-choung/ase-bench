from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# Create ASE database
db = connect('metals.db')

# List of metals
metals = ['Cu', 'Ag', 'Au']

# Store bulk structures and energies
for metal in metals:
    atoms = bulk(metal)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy, formula=metal)

# Query and print results
for row in db.select():
    print(row.formula, row.energy)
