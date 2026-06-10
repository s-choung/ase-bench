from ase.build import bulk
from ase.calculators.emt import EMT
import ase.db

# Create (or open) a database file
db = ase.db.connect('bulk_metals.db')

# Build bulk structures, compute EMT energies and store them
for sym in ('Cu', 'Ag', 'Au'):
    atoms = bulk(sym, 'fcc')
    atoms.set_calculator(EMT())
    e = atoms.get_potential_energy()
    db.write(atoms, energy=e)

# Query all entries and print formula + energy
for row in db.select():
    print(row.formula, row.energy)
