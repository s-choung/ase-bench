from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Connect to (or create) the database file
db = connect('cu_ag Au.db')

# Define bulk structures and calculate their EMT energies
for element, symbol in [('Cu', 'Cu'), ('Ag', 'Ag'), ('Au', 'Au')]:
    atoms = bulk(symbol, cubic=True)
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms, formula=f'{element}', energy=atoms.get_potential_energy())

# Query all entries from the database
entries = list(db.select())

# Print each entry's formula and energy
for entry in entries:
    print(f'Formula: {entry.formula}, Energy (eV): {entry.energy}')
    
db.close()
